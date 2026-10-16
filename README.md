
# OPTiMAR ontology - offshore wind platform

Repository containing the OPTiMAR ontology for offshore wind platforms, including definitions, instances, and usage examples.  
The ontology models platform components, turbines, sensors, failures, maintenance activities, actors, roles, and environmental conditions, supporting semantic interoperability and reasoning for monitoring and operational planning.

---

## Repository structure

- `ontology/` : ontology files organized by version.
- `ontology/alignments/` : alignment module with SAREF and the Open Energy Ontology (not imported by the core ontology).
- `instances/` : example instantiations aligned with each ontology version.
- `queries/` : competency questions formalised as SPARQL queries, and the results obtained on the example instantiation (`RESULTS.md`).
- `scripts/` : `run_cqs.py`, which runs every competency question against the ontology and its instances.
- `docs/` : Widoco documentation served through GitHub Pages (generated with `docs-src/build_docs.sh`).
- `docs-src/` : Widoco configuration and hand-written sections used to build `docs/`.
- `CHANGELOG.md` : detailed changes per version.
- `CONTRIBUTING.md` : how to propose changes, checks, and versioning policy.
- `LICENSE` : repository license file.

---

## Ontology versions

| Version | Description | Release date | URL |
|---------|-------------|--------------|-----|
| v0.1 | Initial version, basic ontology with main classes, properties, and example instances for offshore wind platforms. | 2025-06-05 | [v0.1](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v0.1.ttl) |
| v0.2 | Added detailed sensors, measured data, failures, actors and roles. | 2025-09-24 | [v0.2](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v0.2.ttl) |
| v1.0 | Stable version of the ontology.<br>Consolidation and extension of structural and turbine components.<br>Inclusion of actors and roles with their functional relationships.<br>Detailed definition of specific sensor classes and associated measurement types.<br>More comprehensive modeling of failure events.<br>Inclusion of properties for measured data and environmental conditions. | 2025-10-06 | [v1.0](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v1.0.ttl) |
| v2.0 | Major hierarchy improvements and refactoring.<br>Separation of conceptual `Failure` classes from specific `FailureEvent` classes.<br>Introduction of `ex:Generator` and `ex:StructuralComponent`.<br>Enhanced logical constraints (cardinality, symmetric properties, and inverse relationships).<br>Standardized QUDT usage for physical quantities and property renaming for consistency.| 2025-12-01 | [v2.0](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v2.0.ttl) |
| v2.1 | New Components added: Gearbox and Transformer.<br>Electrical Sensors: ActivePowerSensor, ReactivePowerSensor, CurrentSensor, VoltageSensor, GridFrequencySensor, and TorqueSensor.<br>Rotor Sensors added: RotorSpeedSensor and RotorAngleSensor.<br>Measurement Data for ElectricalData, TemperatureData, and RotorData.<br>Added severity for failure, and relationships causesFailure / precededBy.<br>Added temporal properties startDateTime, endDateTime, detectionDateTime, and duration.<br>Inverse Properties added for traceability | 2026-01-19 | [v2.1](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v2.1.ttl) |
| v2.2 | Control sensors expansion. Added YawSensor (nacelle orientation) and PitchAngleSensor (blade angle). Inclusion of data classes: YawAngleData, PitchAngleData. Definition of measurement and monitoring properties for yaw and pitch with their inverse relationships. | 2026-01-30 | [v2.2](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v2.2.ttl) |
| v2.3 | Wind farms and monitoring reorganization.<br>New `WindFarm` class and platform composition hierarchy (`hasPlatform`, `hasTurbine`, `hasComponent`).<br>New components/sensors: `Inverter`, `ApparentPowerSensor`, `RotationalSpeedSensor`.<br>New measurement classes: `WindData`, `WindSpeedData`, `WindDirectionData`.<br>`monitors`/`monitoredBy`/`measures` become generic top-level properties, with existing `...Monitors`/`...MonitoredBy`/`measures...` properties turned into subproperties (plus new `actorMonitors`, `turbineComponentMonitoredBy`, `measuresWindSpeed`, `measuresWindDirection`).<br>New `isInstalledIn`/`hasInstalled` sensor-component relationship and `measurementType` data property.<br>Consistency fixes for `duration`, `pressureLevel`, `stressLevel`, `vibrationLevel`, and `hasGeneratedData` typing. | 2026-07-13 | [v2.3](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v2.3.ttl) |
| v2.4 | Review-driven release. Ontology IRI `https://w3id.org/optimar` (namespace unchanged), SOSA namespace fixed, valid DCMI metadata, explicit SOSA/PROV-O alignment, SAREF/OEO alignment module. New floating substructure, mooring, anchor and seabed modules; sensor sampling frequency and data format; maintenance-failure relations. Declared `Base`, fixed disjointness axioms. OWL 2 DL. See `CHANGELOG.md`. | 2026-10-16 | [v2.4](https://bisite.github.io/OPTIMAR-Ontology/ontology/OPTiMAR-v2.4.ttl) |


Each version of the ontology is stored in a separate file with its own namespace IRI.  
Full instances for each version are stored under the `instances/` directory.

---

## Documentation

The documentation generated with **Widoco** is served at <https://w3id.org/optimar> (GitHub Pages, `docs/index.html`). It includes the description of every class and property, the changes from the previous version, a WebVOWL visualisation and the ontology serialised in Turtle, RDF/XML, N-Triples and JSON-LD.

---

## Ontology IRI and usage

- Ontology IRI (always the latest release): `https://w3id.org/optimar`
- Version IRI of this release: `https://w3id.org/optimar/2.4`
- Namespace for terms: `https://w3id.org/optimar#` (preferred prefix `optimar`)
- Example instances: `https://bisite.github.io/OPTIMAR-Ontology/instances/v2.4/instances.ttl` (namespace `https://w3id.org/optimar/example#`)

```turtle
@prefix optimar: <https://w3id.org/optimar#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

---

## Competency questions

The 27 competency questions that drive the ontology are in `queries/` as SPARQL files. To run them against the ontology and the example instantiation:

```bash
pip install rdflib
python scripts/run_cqs.py --version 2.4
```

---

## Maintenance and contributions

The ontology is maintained by BISITE (University of Salamanca) and Tekniker. Change requests and bug reports are welcome through [GitHub issues](https://github.com/bisite/OPTIMAR-Ontology/issues); see `CONTRIBUTING.md` for the review process and the versioning policy.

---

## How to cite

Flores, A., Garcia, O., & Aceta, C. (2026). Offshore Wind Power Platform Ontology for OPTiMAR (v2.4). Zenodo. https://doi.org/10.5281/zenodo.17962873

---

## License
This project is distributed under the MIT License.
For more details, please consult the LICENSE file in the repository.
