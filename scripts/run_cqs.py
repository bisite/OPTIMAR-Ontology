#!/usr/bin/env python3
"""Run the OPTiMAR competency questions (queries/CQ*.rq) against the
ontology and its example instantiation.

Usage:
    pip install rdflib
    python scripts/run_cqs.py [--version 2.4] [--show N] [--markdown FILE]

Exit code is 1 if any competency question returns no results.
"""
import argparse
import sys
from pathlib import Path

import rdflib

ROOT = Path(__file__).resolve().parent.parent


def short(term, graph):
    if isinstance(term, rdflib.URIRef):
        try:
            return graph.namespace_manager.normalizeUri(term)
        except Exception:
            return str(term)
    return str(term)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="2.4")
    parser.add_argument("--show", type=int, default=5, help="rows to print per query")
    parser.add_argument("--markdown", help="write a Markdown report to this file")
    args = parser.parse_args()

    graph = rdflib.Graph()
    graph.parse(ROOT / "ontology" / f"OPTiMAR-v{args.version}.ttl", format="turtle")
    graph.parse(ROOT / "instances" / f"v{args.version}" / "instances.ttl", format="turtle")
    graph.bind("ex", "https://w3id.org/optimar/example#")
    graph.bind("unit", "http://qudt.org/vocab/unit/")

    failed = []
    report = [f"# Competency question results (OPTiMAR v{args.version})\n"]
    for path in sorted((ROOT / "queries").glob("CQ*.rq")):
        text = path.read_text(encoding="utf-8")
        question = text.splitlines()[0].lstrip("# ").strip()
        rows = list(graph.query(text))
        status = "OK" if rows else "NO RESULTS"
        if not rows:
            failed.append(path.stem)
        print(f"[{status}] {question} -> {len(rows)} rows")
        report.append(f"## {question}\n\n`{path.name}` returned {len(rows)} row(s).\n")
        if rows:
            header = [str(v) for v in rows[0].labels]
            report.append("| " + " | ".join(header) + " |")
            report.append("|" + "---|" * len(header))
        for row in rows[: args.show]:
            cells = [short(v, graph) if v is not None else "" for v in row]
            print("    " + " | ".join(cells))
            report.append("| " + " | ".join(cells) + " |")
        report.append("")

    if args.markdown:
        Path(args.markdown).write_text("\n".join(report), encoding="utf-8")

    total = len(list((ROOT / "queries").glob("CQ*.rq")))
    print(f"\n{total - len(failed)}/{total} competency questions answered")
    if failed:
        print("Without results:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
