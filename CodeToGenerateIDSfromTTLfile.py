from rdflib import Graph, Namespace, RDF, RDFS
import xml.etree.ElementTree as ET
from xml.dom import minidom

# === SETUP ===

ttl_path = r"C:\OntologyPythonCode\DataDectionaryAndInformationRequirement\LOINforLightingFixture.ttl"
output_path = r"C:\OntologyPythonCode\DataDectionaryAndInformationRequirement\LightingFixture.ids"

g = Graph()
g.parse(ttl_path, format="turtle")

# Namespaces
LOINLF = Namespace("http://www.semanticweb.org/acer/ontologies/2025/3/LOINforLightingSimulation/")
LOIN = Namespace("https://w3id.org/loin#")
TEMPO = Namespace("https://w3id.org/tempo#")
LPPO = Namespace("http://www.w3id.org/ppon/lppo#")
QUDT = Namespace("http://qudt.org/schema/qudt/")
UNIT = Namespace("http://qudt.org/vocab/unit/")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
NS = "http://standards.buildingsmart.org/IDS"

ET.register_namespace("ids", NS)
ET.register_namespace("xs", str(XSD))
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

def ns(tag): return f"{{{NS}}}{tag}"
def get_label(uri): return uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]

# === Extract info from RDF ===

purpose_label = milestone_label = sending_actor = receiving_actor = description_text = ""

for _, _, o in g.triples((None, LOIN.hasPurpose, None)):
    purpose_label = get_label(str(o))
for _, _, o in g.triples((None, LOIN.InformationDeliveryMilestone, None)):
    milestone_label = get_label(str(o))
for _, _, o in g.triples((None, LOIN.SendingActor, None)):
    sending_actor = get_label(str(o))
for _, _, o in g.triples((None, LOIN.ReceivingActor, None)):
    receiving_actor = get_label(str(o))
for subj in g.subjects(RDF.type, Namespace("http://www.w3.org/2002/07/owl#")["Ontology"]):
    for _, _, comment in g.triples((subj, RDFS.comment, None)):
        description_text = str(comment)

# === Build IDS XML ===

ids = ET.Element(ns("ids"), {
    "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "xsi:schemaLocation": f"{NS} {NS}/1.0/ids.xsd"
})

info = ET.SubElement(ids, ns("info"))
ET.SubElement(info, ns("title")).text = "Lighting Fixture Requirements"
ET.SubElement(info, ns("author")).text = "BIM Engineer"
ET.SubElement(info, ns("date")).text = "2025-05-01"
if purpose_label:
    ET.SubElement(info, ns("purpose")).text = purpose_label
if milestone_label:
    ET.SubElement(info, ns("milestone")).text = milestone_label
if description_text:
    ET.SubElement(info, ns("description")).text = description_text

# --- Specification ---
specifications = ET.SubElement(ids, ns("specifications"))
spec = ET.SubElement(specifications, ns("specification"), {
    "name": "LightingFixtureSpecification",
    "ifcVersion": "IFC4"
})
if purpose_label:
    ET.SubElement(spec, ns("purpose")).text = purpose_label
if milestone_label:
    ET.SubElement(spec, ns("milestone")).text = milestone_label
if sending_actor:
    ET.SubElement(spec, ns("sendingActor")).text = sending_actor
if receiving_actor:
    ET.SubElement(spec, ns("receivingActor")).text = receiving_actor

# --- Applicability ---
applicability = ET.SubElement(spec, ns("applicability"), {
    "minOccurs": "1",
    "maxOccurs": "unbounded"
})
entity = ET.SubElement(applicability, ns("entity"))
name = ET.SubElement(entity, ns("name"))
ET.SubElement(name, ns("simpleValue")).text = "IFCLIGHTFIXTURE"

# --- Requirements ---
requirements = ET.SubElement(spec, ns("requirements"))
for group in g.subjects(RDF.type, TEMPO.GroupOfProperties):
    group_label = get_label(str(group))

    for prop in g.objects(group, TEMPO.hasProperty):
        prop_name = get_label(str(prop))

        # Infer RDF datatype
        rdf_range = None
        for _, _, rng in g.triples((prop, RDFS.range, None)):
            rdf_range = str(rng)

        # Default
        ifc_type = "IFCREAL"
        xs_base = "xs:float"

        if rdf_range == str(XSD.string):
            ifc_type = "IFCTEXT"
            xs_base = "xs:string"
        elif rdf_range == str(XSD.boolean):
            ifc_type = "IFCBOOLEAN"
            xs_base = "xs:boolean"

        prop_tag = ET.SubElement(requirements, ns("property"), {
            "cardinality": "required",
            "dataType": ifc_type
        })

        pset_tag = ET.SubElement(prop_tag, ns("propertySet"))
        ET.SubElement(pset_tag, ns("simpleValue")).text = group_label

        base_name = ET.SubElement(prop_tag, ns("baseName"))
        ET.SubElement(base_name, ns("simpleValue")).text = prop_name

        value_tag = ET.SubElement(prop_tag, ns("value"))
        restriction = ET.SubElement(value_tag, "{http://www.w3.org/2001/XMLSchema}restriction", {
            "base": xs_base
        })

        if xs_base == "xs:float":
            ET.SubElement(restriction, "{http://www.w3.org/2001/XMLSchema}minInclusive", value="0")
        elif xs_base == "xs:string":
            ET.SubElement(restriction, "{http://www.w3.org/2001/XMLSchema}minLength", value="1")
        elif xs_base == "xs:boolean":
            ET.SubElement(restriction, "{http://www.w3.org/2001/XMLSchema}enumeration", value="true")
            ET.SubElement(restriction, "{http://www.w3.org/2001/XMLSchema}enumeration", value="false")

# === Save pretty XML ===
xml_str = minidom.parseString(ET.tostring(ids, encoding="utf-8")).toprettyxml(indent="  ")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_str)

print("✅ IDS file saved to:", output_path)
