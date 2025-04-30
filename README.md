# LOIN-for-Lighting-Simulation

This repository supports the thesis project **"Lifting Heterogeneous Data into RDF/OWL Knowledge Graph: A Semantic Approach"** conducted as part of the Master's program in Sustainable Building Information Management at Jönköping University.

## 🧠 Project Summary

The Architecture, Engineering, and Construction (AEC) industry suffers from poor data interoperability, especially when integrating product data like lighting with Building Information Modeling (BIM). This project uses Semantic Web technologies and Linked Data principles to tackle the interoperability issue by:

- Extracting lighting product data.
- Structuring and sharing it using the **LOIN (Level of Information Need)** methodology.
- Receiving simulation results or specification data.
- Validating it against **Information Delivery Specifications (IDS)**.

## 🔍 Objectives

1. Extract lighting data from RDF-based dictionaries.
2. Package and deliver it using LOIN and Data Templates.
3. Support semantic validation with IDS against received data.
4. Use SPARQL for advanced querying and reasoning.

## 🔗 Key Standards and Ontologies

- **ISO 7817 (LOIN)** – Defines level of information need.
- **ISO 23386 & 23387** – Used for data templates and property definition.
- **bSDD** – buildingSMART Data Dictionary for standardized property use.
- **BOT / QUDT / SAREF** – Domain ontologies for building elements and quantities.

## 🚀 Technologies & Tools

- **RDF / OWL** – Knowledge representation.
- **Protégé** – Ontology design and alignment.
- **Python (rdflib)** – RDF transformation and automation.
- **SPARQL / GeoSPARQL** – Semantic querying.
- **GraphDB / Stardog / Fuseki** – Triplestore and query execution.
- **LOIN XML and IDS** – Specification and validation exchange format.

## 🛠 Use Case

The example use case involves sharing lighting data from a manufacturer with an architect:

1. Extract and transform product data into RDF using a predefined ontology.
2. Package the data using the LOIN approach and share it with an architect.
3. Architect selects or simulates lighting parameters and returns data.
4. The data is validated against predefined IDS rules using SHACL or SPARQL.

![Workflow](https://github.com/tamo23uk/LOIN-for-Lighting-Simulation/blob/main/Use-case%20Workflow%20diagram.png) 

## 📖 Documentation

- [Halfway Report (PDF)](./docs/TEBV24_Half-Way-Report.pdf)
- [Ontology Network Reference: Filardo et al. (2024)](./docs/Filardo-A standard-based ontology network-2024.pdf)

## 📚 References

- Kebede et al., 2022. *Integration of manufacturers’ product data using semantic web*.
- Filardo et al., 2024. *A Standard-Based Ontology Network for Information Requirements*.
- ISO 23386, 23387, 7817.

## 🧑‍💼 Authors

- **Mohamad Monir Taktak** – tamo23uk@student.ju.se  
- **Nischal Bhattarai** – bhni23vb@student.ju.se

Supervised by **Rahel Kebede**  
School of Engineering, Jönköping University

---

> 📢 _This repository is a research prototype and not production-ready. Contributions and feedback are welcome._

