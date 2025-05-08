import ifcopenshell
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

# === CONFIGURATION ===
input_ifc_path = "HUSPsetPopulated.ifc"  # Replace with your file path
output_rdf_path = "output_ifcopenshell.ttl"

# === LOAD IFC FILE ===
ifc = ifcopenshell.open(input_ifc_path)

# === SET UP RDF GRAPH ===
g = Graph()
IFC = Namespace("https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#")
EX = Namespace("http://example.org/ifc#")
g.bind("ifc", IFC)
g.bind("ex", EX)

# === CONVERT BASIC IFC ELEMENTS ===
for element in ifc.by_type("IfcRoot"):
    subject = EX[element.GlobalId]
    g.add((subject, RDF.type, IFC[element.is_a()]))
    g.add((subject, IFC.globalId_IfcRoot, Literal(element.GlobalId)))
    if element.Name:
        g.add((subject, IFC.name_IfcRoot, Literal(element.Name)))
    if element.Description:
        g.add((subject, IFC.description_IfcRoot, Literal(element.Description)))

# === HANDLE IfcRelDefinesByProperties and Property Sets ===
for rel in ifc.by_type("IfcRelDefinesByProperties"):
    rel_uri = EX[rel.GlobalId]
    g.add((rel_uri, RDF.type, IFC.IfcRelDefinesByProperties))
    g.add((rel_uri, IFC.globalId_IfcRoot, Literal(rel.GlobalId)))

    for related in rel.RelatedObjects:
        g.add((rel_uri, IFC.relatedObjects_IfcRelDefinesByProperties, EX[related.GlobalId]))

    if rel.RelatingPropertyDefinition:
        pset = rel.RelatingPropertyDefinition
        pset_uri = EX[pset.GlobalId]
        g.add((rel_uri, IFC.relatingPropertyDefinition_IfcRelDefinesByProperties, pset_uri))
        g.add((pset_uri, RDF.type, IFC[pset.is_a()]))
        if pset.Name:
            g.add((pset_uri, IFC.name_IfcRoot, Literal(pset.Name)))

        # === Extract Pset Properties ===
        if hasattr(pset, "HasProperties"):
            for prop in pset.HasProperties:
                # Use a composed URI (not GlobalId)
                prop_uri = EX[f"{pset.GlobalId}_{prop.Name}"]
                g.add((pset_uri, IFC.hasProperties_IfcPropertySet, prop_uri))
                g.add((prop_uri, RDF.type, IFC[prop.is_a()]))
                if prop.Name:
                    g.add((prop_uri, IFC.name_IfcProperty, Literal(prop.Name)))
                if hasattr(prop, "NominalValue") and prop.NominalValue:
                    value = prop.NominalValue.wrappedValue
                    g.add((prop_uri, IFC.nominalValue_IfcPropertySingleValue, Literal(value, datatype=XSD.string)))

# === SAVE TO TTL FILE ===
g.serialize(destination=output_rdf_path, format="turtle")
print(f"✅ RDF exported successfully to: {output_rdf_path}")