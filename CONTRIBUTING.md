# Contributing and governance

The OPTiMAR ontology is maintained by the BISITE group (University of Salamanca) together with Tekniker. Anyone can propose changes.

## How to propose a change

1. Open a [GitHub issue](https://github.com/bisite/OPTIMAR-Ontology/issues) describing the need: the term or axiom affected, a use case or competency question that motivates it, and, if possible, example data.
2. The maintainers discuss the proposal in the issue. Changes to domain definitions are reviewed by at least one domain expert from the project partners.
3. Accepted changes can be submitted as a pull request. A pull request must:
   - edit a new version file `ontology/OPTiMAR-vX.Y.ttl` (released files are never modified);
   - keep labels and comments in English and Spanish;
   - pass the checks below;
   - add an entry to `CHANGELOG.md`.

## Checks

```bash
pip install rdflib
python scripts/run_cqs.py --version X.Y     # all competency questions must return results
```

Consistency and the OWL 2 DL profile are checked with [ROBOT](https://robot.obolibrary.org/):

```bash
robot validate-profile --profile DL --input ontology/OPTiMAR-vX.Y.ttl
robot merge --input ontology/OPTiMAR-vX.Y.ttl --input instances/vX.Y/instances.ttl \
      reason --reasoner HermiT --output /tmp/reasoned.ttl
```

## Versioning

- Term IRIs use the namespace `https://w3id.org/optimar#` and are stable across versions. Terms are never deleted: obsolete terms are marked with `owl:deprecated true` and a pointer to their replacement.
- The ontology IRI `https://w3id.org/optimar` always resolves to the latest release. Each release has a version IRI `https://w3id.org/optimar/X.Y` and is archived in Zenodo.
- A MINOR release (`2.3 → 2.4`) adds terms or fixes axioms. A MAJOR release removes or redefines terms. `owl:priorVersion` links each release to the previous one, and `owl:backwardCompatibleWith` is declared only when data valid for the previous release remains valid.
- Documentation in `docs/` is regenerated for every release with `docs-src/build_docs.sh`.
