# LOIN-for-Lighting-Simulation

This repository supports the thesis project **"Lifting Heterogeneous Data into RDF/OWL Knowledge Graph: A Semantic Approach"** conducted as part of the Master's program in Sustainable Building Information Management at Jönköping University.

## 🧠 Project Summary

The Architecture, Engineering, and Construction (AEC) industry suffers from poor data interoperability during cross-domain integration of diverse data & sources across multiple project stakeholders in a project. Semantic Web technologies and Linked Data Principles are seen as a solution to address these issues by transforming the data into a machine-interpretable format. This project looks into the transformation of heterogeneous data into RDF/OWL data using a semantic approach. It utilizes Semantic Web technologies and Linked Data principles to tackle the interoperability issue by:

- Extracting lighting product data.
- Structuring and sharing it using the **LOIN (Level of Information Need)** methodology.
- Receiving simulation results or specification data.
- Validating it against **Information Delivery Specifications (IDS)**.

## 🔍 Objectives

1. Extract lighting data from RDF-based dictionaries.
2. Package and deliver it using LOIN and Data Templates.
3. Support semantic validation with IDS against received data.
4. Use SPARQL / SHACL for advanced querying and reasoning.

## 🔗 Key Standards and Ontologies

- **Level of Information Need (LOIN) Ontology** – Defines level of information need. <https://w3id.org/loin>
- **Data Template Ontology (TempO)** – Used for data templates and property definition. <https://w3id.org/tempo>
- **ISO 23386 Property Ontology (ISOProps)** –  Describing, creating, and maintenance of properties in interconnected data dictionaries. <https://w3id.org/isoprops>
- **Lighting Product Property Ontology (LPPO)** – Data dictionary for the properties describing electric lighting products and luminaires and sensing devices used in the construction. <http://www.w3id.org/ppon/lppo>

## 🚀 Technologies & Tools

- **RDF / OWL** – Knowledge representation.
- **Protégé** – Ontology design and alignment.
- **Python (rdflib / Stardog RDF Grammars)** – RDF transformation and automation. / Visual Studio Code syntax highlighting for all your favorite RDF languages, and a few Stardog-specific ones, too!
- **SPARQL / SHACL** – Semantic querying.
- **GraphDB / Stardog** – Triplestore and query execution.
- **LOIN XML and IDS** – Specification and validation exchange format.

## 🛠 Use Case

The example use case involves sharing lighting data from a manufacturer with an architect:

1. Extract and transform product data into RDF using a predefined ontology.
2. Package the data using the LOIN approach and share it with an architect.
3. Architect selects or/and simulates lighting parameters and returns data.
4. The data is validated against predefined IDS rules using SHACL or SPARQL.

![Workflow](https://github.com/tamo23uk/LOIN-for-Lighting-Simulation/blob/main/Use-case%20Workflow%20diagram.png) 

## 📖 Documentation

- [Halfway Report (PDF)](./docs/TEBV24_Half-Way-Report.pdf)
- [Ontology Network Reference: Filardo et al. (2024)](./docs/Filardo-A standard-based ontology network-2024.pdf)

## 🗂️ Project Directory Structure

- 📁 ontologies/ contains all semantic definitions (RDF/OWL). Start here to understand data structures.

- 📁 data-exchange/ contains files used for data exchange between stakeholders (e.g., IDS, LOIN Excel).

- 📁 models/ are IFC files used to simulate the building.

- 📁 results/ are generated after validating IFC against IDS using tools like Cobuilder and SHACL.

- 📁 scripts/ contains automation tools, such as transforming .ttl to .ids.

## 📚 References

- Kebede et al., 2022. *Integration of manufacturers’ product data using semantic web*.
- Filardo et al., 2024. *A Standard-Based Ontology Network for Information Requirements*.
- ISO 23386, 23387, 7817.

## 🧑‍💼 Authors

- **Mohamad Monir Taktak** - tamo23uk@student.ju.se  / monertaktak@gmail.com
- **Nischal Bhattarai** - bhni23vb@student.ju.se / nisbhswe@gmail.com

Supervised by 
- **Peter Johansson** - peter.johansson@ju.se
- **Rahel Kebede**  - rahel.kebede@ju.se
School of Engineering, Jönköping University

---

> 📢 This repository is a research prototype and not production-ready. Contributions and feedback are welcome.

