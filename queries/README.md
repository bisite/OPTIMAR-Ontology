# Competency questions

Each `CQxx.rq` file formalises one competency question as a SPARQL query. The first line of each file states the question and its thematic area:

| Area | CQs |
|---|---|
| Structural components and mechanical properties | CQ01–CQ07 |
| Floating substructure, mooring systems and seabed | CQ08–CQ13 |
| Sensing, failure prediction and data management | CQ14–CQ22 |
| Actors, roles and operations | CQ23–CQ25 |
| Use cases: predictive maintenance (CQ26) and operational optimisation (CQ27) | CQ26–CQ27 |

`RESULTS.md` contains the results obtained on the example instantiation of the current version. To regenerate it:

```bash
python scripts/run_cqs.py --version 2.4 --show 20 --markdown queries/RESULTS.md
```
