
# OPTiMAR ontology - offshore wind platform

Repository containing the OPTiMAR ontology for offshore wind platforms, including definitions, instances, and usage examples.  
The ontology models platform components, turbines, sensors, failures, maintenance activities, actors, roles, and environmental conditions, supporting semantic interoperability and reasoning for monitoring and operational planning.

---

## repository structure

- `ontology/` : ontology files organized by version.
- `instances/` : full instantiations aligned with each ontology version.
- `scripts/` : auxiliary scripts for validation, SPARQL queries, or ontology processing.
- `docs/` : ontology documentation, diagrams, and metadata.
- `LICENSE` : repository license file.
- `README.md` : this file.

---

## ontology versions

| Version | Description                                                                                                         | Release date  | URL                                                                           |
|---------|---------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------|
| v0.1    | Initial version, basic ontology with main classes, properties, and example instances for offshore wind platforms.   | 2025-06-05    | [v0.1](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v0.1.ttl)   |
|---------|---------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------|
| v0.2    | Added detailed sensors, measured data, failures, actors and roles.                                                  | 2025-09-24    | [v0.2](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v0.2.ttl)   |
|---------|---------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------|
| v1.0    | Stable version of the ontology. Consolidation and extension of structural and turbine components.                   | 2025-10-06    | [v1.0](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v1.0.ttl)   |
|         | Inclusion of actors and roles with their functional relationships.                                                  |               |                                                                               |
|         | Detailed definition of specific sensor classes and associated measurement types.                                    |               |                                                                               |
|         | More comprehensive modeling of failure events.                                                                      |               |                                                                               |
|         | Inclusion of properties for measured data and environmental conditions.                                             |               |                                                                               |
|---------|---------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------|

Each version of the ontology is stored in a separate file with its own namespace IRI.  
Full instances for each version are stored under the `instances/` directory.

---

## ontology IRI and usage

For version 0.1:

- Ontology TTL: `https://bisite.github.io/OPTIMAR-Ontology/ontology/v0.1/OPTiMAR-v0.1.ttl`
- Instances TTL: `https://bisite.github.io/OPTIMAR-Ontology/instances/v0.1/instances.ttl`

The ontology uses the following common prefixes:

```turtle
@prefix ex: <https://bisite.github.io/OPTIMAR-Ontology/ontology/v0.1/OPTiMAR-v0.1.ttl#> .
@prefix sosa: <https://www.w3.org/ns/sosa/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

---

## License
This project is distributed under the MIT License.
For more details, please consult the LICENSE file in the repository.
