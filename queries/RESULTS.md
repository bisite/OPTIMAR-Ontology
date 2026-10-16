# Competency question results (OPTiMAR v2.4)

## CQ01 [Structural components] What are the main components of an offshore wind platform?

`CQ01.rq` returned 11 row(s).

| platform | component | type |
|---|---|---|
| ex:OptimarPlatform01 | ex:Base01 | optimar:Base |
| ex:OptimarPlatform01 | ex:Blade01 | optimar:Blade |
| ex:OptimarPlatform01 | ex:Blade02 | optimar:Blade |
| ex:OptimarPlatform01 | ex:Blade03 | optimar:Blade |
| ex:OptimarPlatform01 | ex:FloatingSubstructure01 | optimar:FloatingSubstructure |
| ex:OptimarPlatform01 | ex:Hub01 | optimar:Hub |
| ex:OptimarPlatform01 | ex:MooringSystem01 | optimar:CatenaryMooringSystem |
| ex:OptimarPlatform01 | ex:MooringSystem01 | optimar:PermanentMooringSystem |
| ex:OptimarPlatform01 | ex:Nacelle01 | optimar:Nacelle |
| ex:OptimarPlatform01 | ex:Tower01 | optimar:Tower |
| ex:OptimarPlatform01 | ex:Turbine01 | optimar:Turbine |

## CQ02 [Structural components] What are the aerodynamic and mechanical properties of the blade?

`CQ02.rq` returned 7 row(s).

| blade | property | value | unit |
|---|---|---|---|
| ex:Blade01 | optimar:elasticModulus | 135 | unit:GigaPA |
| ex:Blade01 | optimar:externalShape | Aerodinámica |  |
| ex:Blade01 | optimar:length | 90 | unit:M |
| ex:Blade01 | optimar:mass | 65000 | unit:KiloGM |
| ex:Blade01 | optimar:material | Fibra de Carbono |  |
| ex:Blade01 | optimar:reinforcementType | Largueros de fibra de carbono y almas de fibra de vidrio |  |
| ex:Blade01 | optimar:stiffness | 18000000000 | unit:N-M2 |

## CQ03 [Structural components] What are the mechanical properties of the hub?

`CQ03.rq` returned 3 row(s).

| hub | property | value | unit |
|---|---|---|---|
| ex:Hub01 | optimar:diameter | 5 | unit:M |
| ex:Hub01 | optimar:mass | 190000 | unit:KiloGM |
| ex:Hub01 | optimar:momentOfInertia | 980000 | unit:KiloGM-M2 |

## CQ04 [Structural components] What are the mechanical properties of the nacelle (mass, generator speed)?

`CQ04.rq` returned 1 row(s).

| nacelle | mass | massUnit | generator | speed | speedUnit |
|---|---|---|---|---|---|
| ex:Nacelle01 | 630000 | unit:KiloGM | ex:Generator01 | 1800 | unit:REV-PER-MIN |

## CQ05 [Structural components] What are the mechanical properties of the tower?

`CQ05.rq` returned 4 row(s).

| tower | property | value | unit |
|---|---|---|---|
| ex:Tower01 | optimar:diameter | 10 | unit:M |
| ex:Tower01 | optimar:height | 120 | unit:M |
| ex:Tower01 | optimar:material | Acero estructural S355 |  |
| ex:Tower01 | optimar:thickness | 80 | unit:MilliM |

## CQ06 [Structural components] What are the hydrodynamic and mechanical properties of the floating substructure (incl. connection points)?

`CQ06.rq` returned 1 row(s).

| fs | draft | volume | members | connectionPoints |
|---|---|---|---|---|
| ex:FloatingSubstructure01 | 20 | 15000 | 9 | 3 |

## CQ07 [Structural components] What are the main characteristics of the mooring system (anchors, lines, connectors, tensioners)?

`CQ07.rq` returned 6 row(s).

| mooring | elementType | count |
|---|---|---|
| ex:MooringSystem01 | optimar:MooringLine | 3 |
| ex:MooringSystem01 | optimar:DragEmbedmentAnchor | 2 |
| ex:MooringSystem01 | optimar:SuctionPileAnchor | 1 |
| ex:MooringSystem01 | optimar:MooringConnector | 1 |
| ex:MooringSystem01 | optimar:Tensioner | 1 |
| ex:MooringSystem01 | optimar:Fairlead | 3 |

## CQ08 [Substructure & mooring] What are the structural members of a floating substructure?

`CQ08.rq` returned 9 row(s).

| fs | member | memberType |
|---|---|---|
| ex:FloatingSubstructure01 | ex:Brace01 | optimar:Brace |
| ex:FloatingSubstructure01 | ex:Brace02 | optimar:Brace |
| ex:FloatingSubstructure01 | ex:Brace03 | optimar:Brace |
| ex:FloatingSubstructure01 | ex:Column01 | optimar:Column |
| ex:FloatingSubstructure01 | ex:Column02 | optimar:Column |
| ex:FloatingSubstructure01 | ex:Column03 | optimar:Column |
| ex:FloatingSubstructure01 | ex:HeavePlate01 | optimar:HeavePlate |
| ex:FloatingSubstructure01 | ex:HeavePlate02 | optimar:HeavePlate |
| ex:FloatingSubstructure01 | ex:HeavePlate03 | optimar:HeavePlate |

## CQ09 [Substructure & mooring] What types of anchors exist and how are they classified? (schema-level query)

`CQ09.rq` returned 7 row(s).

| anchorType | label | parent |
|---|---|---|
| optimar:DeadWeightAnchor | Dead Weight Anchor | optimar:Anchor |
| optimar:DragEmbedmentAnchor | Drag Embedment Anchor (DEA) | optimar:Anchor |
| optimar:DrivenPileAnchor | Driven Pile Anchor | optimar:Anchor |
| optimar:GravityInstalledAnchor | Gravity Installed Anchor | optimar:Anchor |
| optimar:SuctionEmbeddedPlateAnchor | Suction Embedded Plate Anchor (SEPLA) | optimar:Anchor |
| optimar:SuctionPileAnchor | Suction Pile Anchor | optimar:Anchor |
| optimar:VerticalLoadAnchor | Vertical Load Anchor (VLA) | optimar:DragEmbedmentAnchor |

## CQ10 [Substructure & mooring] What are the relevant properties of the seabed?

`CQ10.rq` returned 1 row(s).

| location | seabed | soil | sediment | sedimentUnit | inclination | inclinationUnit |
|---|---|---|---|---|---|---|
| ex:NorthSeaLocation | ex:Seabed01 | Arcilla | 12 | unit:M | 2 | unit:DEG |

## CQ11 [Substructure & mooring] What are the mechanical properties of anchors (anchor load, transport load, fatigue)?

`CQ11.rq` returned 3 row(s).

| anchor | anchorLoad | transportLoad | unit | fatigue |
|---|---|---|---|---|
| ex:Anchor01 | 3500 | 250 | unit:KiloN |  |
| ex:Anchor02 |  |  |  |  |
| ex:Anchor03 |  |  |  |  |

## CQ12 [Substructure & mooring] How are mooring systems classified by duration and configuration?

`CQ12.rq` returned 2 row(s).

| mooring | classification |
|---|---|
| ex:MooringSystem01 | optimar:CatenaryMooringSystem |
| ex:MooringSystem01 | optimar:PermanentMooringSystem |

## CQ13 [Substructure & mooring] What are the possible distributions of mooring lines, and which one does each system use?

`CQ13.rq` returned 3 row(s).

| distribution | label | usedBy |
|---|---|---|
| optimar:SinglePointDistribution | Single-point mooring |  |
| optimar:EvenlyDistributed | Evenly distributed | ex:MooringSystem01 |
| optimar:ClusteredDistribution | Clustered |  |

## CQ14 [Sensing & failures] What data are needed to predict failures? (data observed on components affected by each failure type)

`CQ14.rq` returned 7 row(s).

| failureType | component | dataType |
|---|---|---|
| optimar:Corrosion | ex:Blade01 | optimar:PitchAngleData |
| optimar:Corrosion | ex:Tower01 | optimar:VibrationData |
| optimar:Corrosion | ex:Tower01 | optimar:StressData |
| optimar:MaterialFatigue | ex:Blade01 | optimar:PitchAngleData |
| optimar:MaterialFatigue | ex:Gearbox01 | optimar:VibrationData |
| optimar:MaterialFatigue | ex:Gearbox01 | optimar:TemperatureData |
| optimar:MaterialFatigue | ex:Gearbox01 | optimar:RotorSpeedData |

## CQ15 [Sensing & failures] Which sensors produce the relevant measurements, and on which component are they installed?

`CQ15.rq` returned 10 row(s).

| sensor | sensorType | component |
|---|---|---|
| ex:Anemometer01 | optimar:Anemometer | ex:Nacelle01 |
| ex:ApparentPowerSensor01 | optimar:ApparentPowerSensor | ex:Inverter01 |
| ex:CorrosionCam01 | optimar:CorrosionCamera | ex:Hub01 |
| ex:CorrosionCam02 | optimar:CorrosionCamera | ex:FloatingSubstructure01 |
| ex:VibrationSensor01 | optimar:DynamicMonitor | ex:Tower01 |
| ex:VibrationSensor02 | optimar:DynamicMonitor | ex:Nacelle01 |
| ex:GearboxVibrationSensor01 | optimar:DynamicMonitor | ex:Gearbox01 |
| ex:GaugeSystem01 | optimar:GaugeSystem | ex:Tower01 |
| ex:ISUM01 | optimar:ISUMSystem | ex:FloatingSubstructure01 |
| ex:RotationalSpeedSensor01 | optimar:RotationalSpeedSensor | ex:Gearbox01 |

## CQ16 [Sensing & failures] Which property (type of data) does each sensor measure, and what does it monitor?

`CQ16.rq` returned 34 row(s).

| sensor | dataType | monitored |
|---|---|---|
| ex:Anemometer01 | optimar:WindSpeedData |  |
| ex:Anemometer01 | optimar:WindDirectionData |  |
| ex:CorrosionCam01 |  | ex:Blade01 |
| ex:CorrosionCam02 |  | ex:Tower01 |
| ex:CurrentSensor01 | optimar:CurrentData |  |
| ex:FreqSensor01 | optimar:FrequencyData |  |
| ex:GaugeSystem01 | optimar:StressData |  |
| ex:GaugeSystem01 |  | ex:Tower01 |
| ex:GearboxVibrationSensor01 | optimar:VibrationData |  |
| ex:GearboxVibrationSensor01 |  | ex:Gearbox01 |
| ex:ISUM01 |  | ex:FloatingSubstructure01 |
| ex:PitchSensor01 | optimar:PitchAngleData |  |
| ex:PitchSensor01 |  | ex:Blade01 |
| ex:PitchSensor02 | optimar:PitchAngleData |  |
| ex:PitchSensor02 |  | ex:Blade02 |
| ex:PitchSensor03 | optimar:PitchAngleData |  |
| ex:PitchSensor03 |  | ex:Blade03 |
| ex:PowerSensor01 | optimar:PowerData |  |
| ex:ReactivePowerSensor01 | optimar:PowerData |  |
| ex:StructuralCam01 |  | ex:Tower01 |

## CQ17 [Sensing & failures] At what frequency are measurements generated?

`CQ17.rq` returned 10 row(s).

| sensor | frequency | unit |
|---|---|---|
| ex:GaugeSystem01 | 50 | unit:HZ |
| ex:GearboxVibrationSensor01 | 25 | unit:HZ |
| ex:ISUM01 | 1 | unit:PER-DAY |
| ex:CorrosionCam01 | 1 | unit:PER-MIN |
| ex:CorrosionCam02 | 1 | unit:PER-MIN |
| ex:Anemometer01 | 1 | unit:PER-MIN |
| ex:TempSensor_Generator | 0.5 | unit:PER-MIN |
| ex:TempSensor_Gearbox | 0.5 | unit:PER-MIN |
| ex:PowerSensor01 | 0.1 | unit:PER-MIN |
| ex:YawSensor01 | 0.1 | unit:PER-MIN |

## CQ18 [Sensing & failures] In which format are sensor measurements presented?

`CQ18.rq` returned 7 row(s).

| format | sensors |
|---|---|
| JPG | CorrosionCam01, CorrosionCam02 |
| CSV | Anemometer01, VibrationSensor01, VibrationSensor02, GearboxVibrationSensor01 |
| TXT | GaugeSystem01 |
| Modbus | TempSensor_Generator, TempSensor_Gearbox |
| JSON | PowerSensor01, ReactivePowerSensor01, VoltageSensor01, CurrentSensor01, FreqSensor01, YawSensor01 |
| binary (float32) | ISUM01 |
| MP4 | StructuralCam01 |

## CQ19 [Sensing & failures] How many units of each sensor type are installed?

`CQ19.rq` returned 19 row(s).

| sensorType | units |
|---|---|
| optimar:TemperatureSensor | 5 |
| optimar:DynamicMonitor | 3 |
| optimar:PitchAngleSensor | 3 |
| optimar:CorrosionCamera | 2 |
| optimar:StructuralCamera | 1 |
| optimar:Anemometer | 1 |
| optimar:ISUMSystem | 1 |
| optimar:GaugeSystem | 1 |
| optimar:ActivePowerSensor | 1 |
| optimar:ReactivePowerSensor | 1 |
| optimar:ApparentPowerSensor | 1 |
| optimar:CurrentSensor | 1 |
| optimar:VoltageSensor | 1 |
| optimar:GridFrequencySensor | 1 |
| optimar:TorqueSensor | 1 |
| optimar:RotorSpeedSensor | 1 |
| optimar:RotorAngleSensor | 1 |
| optimar:RotationalSpeedSensor | 1 |
| optimar:YawSensor | 1 |

## CQ20 [Sensing & failures] Which sensors monitor the temperature of the nacelle?

`CQ20.rq` returned 1 row(s).

| sensor | sensorType |
|---|---|
| ex:TempSensor_Nacelle | optimar:TemperatureSensor |

## CQ21 [Sensing & failures] Which failures affect turbine blades, with which severity and when were they detected?

`CQ21.rq` returned 2 row(s).

| blade | failure | failureType | severity | detectionDate |
|---|---|---|---|---|
| ex:Blade01 | ex:BladeCorrosionFailure | optimar:Corrosion | medium | 2026-01-15T14:30:00+00:00 |
| ex:Blade01 | ex:BladeFatigueFailure | optimar:MaterialFatigue | high | 2026-01-18T10:15:00+00:00 |

## CQ22 [Sensing & failures] What electrical parameters are monitored for the generator, and what are their latest values?

`CQ22.rq` returned 4 row(s).

| sensor | dataType | value | unit |
|---|---|---|---|
| ex:PowerSensor01 | optimar:PowerData | 14.2 | MW |
| ex:VoltageSensor01 | optimar:VoltageData | 690 | V |
| ex:CurrentSensor01 | optimar:CurrentData | 1250 | A |
| ex:FreqSensor01 | optimar:FrequencyData | 50.02 | Hz |

## CQ23 [Actors & operations] Which actors are involved in operating the platform and which roles do they play?

`CQ23.rq` returned 4 row(s).

| actor | actorType | role | roleType |
|---|---|---|---|
| ex:Operator01 | optimar:MaintenanceOperator | ex:TechnicalRole01 | optimar:TechnicalRole |
| ex:CloudAdmin01 | optimar:CloudAdministrator | ex:ManagementRole01 | optimar:ManagementRole |
| ex:Analyst01 | optimar:DataAnalyst | ex:AnalyticalRole01 | optimar:AnalyticalRole |
| ex:ParkOwner01 | optimar:ParkOwner | ex:ManagementRole01 | optimar:ManagementRole |

## CQ24 [Actors & operations] What does each actor monitor, adjust, analyse or manage?

`CQ24.rq` returned 11 row(s).

| actor | relation | target |
|---|---|---|
| ex:Analyst01 | optimar:analyzes | ex:CorrosionEvent01 |
| ex:Analyst01 | optimar:analyzes | ex:BladeCorrosionFailure |
| ex:Analyst01 | optimar:analyzes | ex:YawAngleData01 |
| ex:Analyst01 | optimar:analyzes | ex:GearboxVibrationData01 |
| ex:Analyst01 | optimar:analyzes | ex:GearboxBearingFatigue |
| ex:CloudAdmin01 | optimar:manages | ex:OptimarPlatform01 |
| ex:Operator01 | optimar:actorMonitors | ex:Anemometer01 |
| ex:Operator01 | optimar:actorMonitors | ex:YawSensor01 |
| ex:Operator01 | optimar:performsTask | ex:RoutineInspection01 |
| ex:ParkOwner01 | optimar:manages | ex:OptimarWindFarm01 |
| ex:ParkOwner01 | optimar:manages | ex:OptimarPlatform01 |

## CQ25 [Actors & operations] Which maintenance activities were performed, by whom, on which failure and how long did they take?

`CQ25.rq` returned 3 row(s).

| maintenance | actor | failure | component | start | duration | unit |
|---|---|---|---|---|---|---|
| ex:BladeRepair01 | ex:Operator01 | ex:BladeCorrosionFailure | ex:Blade01 | 2026-01-20T08:00:00+00:00 | 8.5 | unit:HR |
| ex:TowerInspection01 | ex:Operator01 | ex:TowerCorrosionFailure | ex:Tower01 | 2026-01-22T09:00:00+00:00 | 3 | unit:HR |
| ex:GearboxBearingReplacement01 | ex:Operator01 | ex:GearboxBearingFatigue | ex:Gearbox01 | 2026-01-30T16:00:00+00:00 | 2.5 | unit:HR |

## CQ26 [Predictive maintenance] Which observation, sensor and failure triggered each maintenance activity? (observation -> event -> failure -> maintenance)

`CQ26.rq` returned 3 row(s).

| maintenance | event | failure | component | sensor | observation | value | unit |
|---|---|---|---|---|---|---|---|
| ex:BladeRepair01 | ex:CorrosionEvent01 | ex:BladeCorrosionFailure | ex:Blade01 | ex:CorrosionCam01 |  |  |  |
| ex:TowerInspection01 | ex:CorrosionEvent02 | ex:TowerCorrosionFailure | ex:Tower01 | ex:CorrosionCam02 |  |  |  |
| ex:GearboxBearingReplacement01 | ex:GearboxFailureEvent01 | ex:GearboxBearingFatigue | ex:Gearbox01 | ex:GearboxVibrationSensor01 | ex:Observation_Vibration_Gearbox | 8.5 | unit:MilliM-PER-SEC |

## CQ27 [Operational optimisation] Which environmental conditions are associated with failures, and what wind conditions were measured?

`CQ27.rq` returned 2 row(s).

| failure | component | condition | windSpeed | windDirection |
|---|---|---|---|---|
| ex:BladeCorrosionFailure | ex:Blade01 | ex:CurrentWindCondition | 12.5 | 280 |
| ex:TowerCorrosionFailure | ex:Tower01 | ex:CurrentWindCondition | 12.5 | 280 |
