# List All Property Names and Values for IfcLightFixtures

PREFIX ifc: <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT 
  (STR(?fixture) AS ?fixtureID) 
  (STR(?psetName) AS ?psetNameClean) 
  (STR(?propName) AS ?propertyName) 
  (STR(?propValue) AS ?value)
WHERE {
  ?fixture rdf:type ifc:IfcLightFixture .

  ?relDef rdf:type ifc:IfcRelDefinesByProperties ;
          ifc:relatedObjects_IfcRelDefinesByProperties ?fixture ;
          ifc:relatingPropertyDefinition_IfcRelDefinesByProperties ?pset .

  ?pset rdf:type ifc:IfcPropertySet ;
        ifc:name_IfcRoot ?psetName ;
        ifc:hasProperties_IfcPropertySet ?prop .

  ?prop rdf:type ifc:IfcPropertySingleValue ;
        ifc:name_IfcProperty ?propName ;
        ifc:nominalValue_IfcPropertySingleValue ?propValue .
}
ORDER BY ?fixtureID ?psetNameClean ?propertyName


# This query retrieves all light fixture with luminous flux greater than 3000.
PREFIX ifc: <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#>
PREFIX lppo: <http://www.w3id.org/ppon/lppo#>

SELECT ?fixture ?flux
WHERE {
  ?fixture a ifc:IfcLightFixture ;
           lppo:luminousFlux ?flux .
  FILTER (?flux > 3000)
}