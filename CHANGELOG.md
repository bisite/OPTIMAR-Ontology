# Changelog

All notable changes to the OPTiMAR ontology are documented in this file.
Versions follow `MAJOR.MINOR`: a MINOR release adds terms or fixes axioms; a MAJOR release removes or redefines terms. Each release is published at `https://w3id.org/optimar/<version>` and archived in Zenodo.

## [2.4] - 2026-10-16

### Changed (may affect existing data)
- The ontology IRI is now `https://w3id.org/optimar` (without `#`). The namespace for terms is still `https://w3id.org/optimar#`, so term IRIs do not change.
- Fixed the SOSA namespace: `https://www.w3.org/ns/sosa/` → `http://www.w3.org/ns/sosa/`. Data that used the wrong namespace must be updated.
- `measuresTemperatureOf` and `measuresWind` are now subproperties of `monitors` instead of `measures`. `measures` now has domain `sosa:Sensor` and range `Data`: it links a sensor to the data it produces, while `monitors` links a sensor or actor to the monitored entity.
- `performedBy` now has domain `Task` (it was `Maintenance`) and is the inverse of `performsTask`. `Maintenance` is now a subclass of `Task`.
- `requiresMaintenance` now has domain `Component` (it was `TurbineComponent`).
- `houses`, `isHousedIn` and `precededBy` are now transitive (`owl:TransitiveProperty`).
- `monitors`, `monitoredBy` and `hasGeneratedData` now declare domain and range.
- `operationalStatus` (free text) is deprecated (`owl:deprecated true`) in favour of `hasOperationalState`.
- Example instances moved from the ontology namespace to `https://w3id.org/optimar/example#` (prefix `ex:`).

### Fixed
- Declared the `Base` class, used in the definition of `StructuralComponent` since v2.0 but never declared.
- Removed the disjointness axioms between `CorrosionEvent` (an event) and the failure classes `MaterialFatigue` and `Misalignment`. Disjointness between failure types is now a single `owl:AllDisjointClasses` axiom (`Corrosion`, `MaterialFatigue`, `Misalignment`, `Deformation`).
- Added `rdf:type owl:Restriction` to the restrictions on `Hub`, `Nacelle`, `Blade` and `Tower`, and `rdf:type owl:Class` to anonymous unions.
- Metadata: replaced `dc:name` and `dcterms:status`, which are not DCMI terms, with `dcterms:title` and `bibo:status`. All metadata now uses DCMI Terms. Removed the reference to the non-existent term `optimar:changelog`.
- Declared every annotation property and every reused external term: the ontology is now in the OWL 2 DL profile.
- `rdfs:isDefinedBy` for the reused external terms; `dcterms:source` and `foaf:logo` (project logo in `images/`) in the ontology metadata.
- Fixed typos in labels and comments.

### Added
- Alignments with reused vocabularies:
  - SOSA: `madeBySensor ⊑ sosa:madeBySensor`, `isInstalledIn ⊑ sosa:isHostedBy`, `hasInstalled ⊑ sosa:hosts`, `Component` and `EnvironmentalCondition ⊑ sosa:FeatureOfInterest`, `Data ⊑ sosa:Result`.
  - PROV-O: `Actor ⊑ prov:Agent`, `Task` and `Event ⊑ prov:Activity`, `Data ⊑ prov:Entity`, `performedBy ⊑ prov:wasAssociatedWith`, `triggeredBy ⊑ prov:wasInformedBy`.
- Separate alignment module `ontology/alignments/OPTiMAR-alignments-v2.4.ttl` with SAREF core (logical) and OEO (SKOS) mappings.
- Floating substructure members: `SubstructureMember`, `Column`, `HeavePlate`, `Brace`; properties `hasMember`/`isMemberOf`, `draft`, `displacedVolume`.
- Mooring system: `MooringComponent`, `MooringLine`, `Anchor` (+ `DeadWeightAnchor`, `DrivenPileAnchor`, `DragEmbedmentAnchor`, `VerticalLoadAnchor`, `SuctionPileAnchor`, `GravityInstalledAnchor`, `SuctionEmbeddedPlateAnchor`), `MooringConnector`, `Tensioner`, `Fairlead`; classification by configuration (`CatenaryMooringSystem`, `TautLegMooringSystem`, `TensionLegMooringSystem`) and duration (`TemporaryMooringSystem`, `PermanentMooringSystem`); `MooringLineDistribution` with the individuals `SinglePointDistribution`, `EvenlyDistributed`, `ClusteredDistribution`; properties `hasMooringComponent`, `hasMooringLine`, `hasAnchor`, `hasLineDistribution`, `numberOfMooringLines`, `lineTension`, `anchorLoad`, `transportLoad`, `anchoredIn`.
- Site: `Seabed`, `hasSeabed`, `soilComposition`, `sedimentThickness`, `seabedInclination`, `waterDepth`.
- Mechanical properties: `stiffness`, `elasticModulus`, `momentOfInertia`, `reinforcementType`.
- Sensor acquisition metadata: `samplingFrequency`, `dataFormat`.
- Maintenance: `addressesFailure`, `triggeredBy`.
- Disjointness between top-level classes.
- Competency questions as SPARQL queries (`queries/`), a script to run them (`scripts/run_cqs.py`) and an extended example instantiation.

## [2.3] - 2026-07-13
- Added `WindFarm` and the composition hierarchy `WindFarm → WindPowerPlatform → Turbine/Component` (`hasPlatform`, `hasTurbine`, `hasComponent`).
- Added `Inverter`, `ApparentPowerSensor`, `RotationalSpeedSensor`, `WindData`, `WindSpeedData`, `WindDirectionData`.
- `monitors`/`monitoredBy`/`measures` became generic superproperties; existing specific properties became subproperties (plus `actorMonitors`, `turbineComponentMonitoredBy`, `measuresWindSpeed`, `measuresWindDirection`).
- Added `isInstalledIn`/`hasInstalled` and `measurementType`.
- Consistency fixes for `duration`, `pressureLevel`, `stressLevel`, `vibrationLevel` and `hasGeneratedData`.

## [2.2] - 2026-01-30
- Control sensors: `YawSensor`, `PitchAngleSensor`, with `YawAngleData`, `PitchAngleData` and the properties `measuresYawAngle`, `measuresPitchAngle`, `yawAngleMonitoredBy`/`monitorsYawOf`, `pitchAngleMonitoredBy`/`monitorsPitchOf`.

## [2.1] - 2026-01-19
- Components `Gearbox` and `Transformer`.
- Electrical sensors (`ElectricalSensor` and 6 subclasses), rotor sensors (`RotorSensor`, `RotorSpeedSensor`, `RotorAngleSensor`), `TemperatureSensor`.
- Data classes `ElectricalData`, `TemperatureData`, `RotorData` and subclasses.
- Failure `severity`, `causesFailure`, `precededBy`; temporal properties `startDateTime`, `endDateTime`, `detectionDateTime`, `duration`.
- `OperationalState` and `hasOperationalState`; disjointness between top-level sensor classes.

## [2.0] - 2025-12-01
- Persistent W3ID namespace `https://w3id.org/optimar#`.
- Separation of `Failure` classes from `FailureEvent` classes.
- `Generator` and `StructuralComponent`; cardinality restrictions on `Turbine`; symmetric and inverse properties.
- QUDT used consistently for physical quantities.

## [1.0] - 2025-10-06
- First stable release: consolidated structural and turbine components, actors and roles, sensor classes and measurement types, failure events, environmental conditions.

## [0.2] - 2025-09-24
- Reuse of QUDT, PROV-O and VANN; bilingual (English/Spanish) labels and comments; sensors, measured data, failures, actors and roles.

## [0.1] - 2025-06-05
- Initial version with the main classes and properties.
