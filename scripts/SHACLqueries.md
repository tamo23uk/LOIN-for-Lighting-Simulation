# SHACLForLuminousFluxLessthan3000

@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ifc: <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#> .
@prefix lppo: <http://www.w3id.org/ppon/lppo#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <http://example.org/shapes#> .

#SHACL Validation For LightFixture Wit luminous flux less than 3000

ex:HighFluxFixtureShape a sh:NodeShape ;
    sh:targetClass ifc:IfcLightFixture ;
    sh:property [
        sh:path lppo:luminousFlux ;
        sh:datatype xsd:float ;
        sh:minInclusive 3000.01 ;
        sh:message "luminousFlux must be greater than 3000." ;
    ] .




# SHACLValidationForLOIN

@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix lppo: <http://www.w3id.org/ppon/lppo#> .
@prefix loinlf: <http://www.semanticweb.org/acer/ontologies/2025/3/LOINforLightingSimulation/> .
@prefix tempo: <https://w3id.org/tempo#> .
@prefix ex: <http://example.org/shapes#> .
@prefix ifc: <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#> .

ex:LightingFixtureShape
    a sh:NodeShape ;
    sh:targetClass ifc:IfcLightFixture ;

    # Functional Requirements
    sh:property [
        sh:path lppo:illuminanceRange ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path lppo:GlareIndexUGR ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;

    # Simulation Requirements
    sh:property [
        sh:path loinlf:SimulatedIlluminance ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path loinlf:DaylightAutonomy ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path loinlf:AnnualSunlightExposure ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;

    # Product Requirements
    sh:property [
        sh:path lppo:luminousFlux ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path lppo:powerConsumption ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path lppo:mountingType ;
        sh:datatype xsd:string ;
        sh:minLength 1 ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path lppo:correlatedColorTemperature ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path lppo:colorRenderingIndex ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path lppo:averageRatedLifeOfLightSource ;
        sh:datatype xsd:float ;
        sh:minCount 1 ;
    ] .




# This SHACL shape validates that each IfcLightFixture has an averageRatedLifeOfLightSource greater than 40,000 and an illuminanceRange less than 350, both as xsd:float values.

@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ifc: <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#> .
@prefix lppo: <http://www.w3id.org/ppon/lppo#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <http://example.org/shapes#> .

ex:LightFixtureAdvancedValidationShape
    a sh:NodeShape ;
    sh:targetClass ifc:IfcLightFixture ;

    # Constraint: averageRatedLifeOfLightSource > 40000
    sh:property [
        sh:path lppo:averageRatedLifeOfLightSource ;
        sh:datatype xsd:float ;
        sh:minExclusive 40000 ;
        sh:message "averageRatedLifeOfLightSource must be greater than 40000." ;
    ] ;

    # Constraint: illuminanceRange < 350
    sh:property [
        sh:path lppo:illuminanceRange ;
        sh:datatype xsd:float ;
        sh:maxExclusive 350 ;
        sh:message "illuminanceRange must be less than 350." ;
    ] .


# This SHACL shape validates each ifcLightFixture has mounting type Ceiling and Illuminance Range less than 350.

@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ifc: <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2/OWL#> .
@prefix lppo: <http://www.w3id.org/ppon/lppo#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <http://example.org/shapes#> .

ex:LightFixtureAdvancedValidationShape
    a sh:NodeShape ;
    sh:targetClass ifc:IfcLightFixture ;

    # Constraint: averageRatedLifeOfLightSource > 40000
    sh:property [
        sh:path lppo:mountingType ;
        sh:datatype xsd:string ;
        sh:hasValue "Ceiling" ;
        sh:message "Mounting type should be Ceiling." ;
    ] ;
# Constraint: illuminanceRange < 350
    sh:property [
        sh:path lppo:illuminanceRange ;
        sh:datatype xsd:float ;
        sh:maxExclusive 350 ;
        sh:message "illuminanceRange must be less than 350." ;
    ] .



