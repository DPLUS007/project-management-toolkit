# ERP/COTS Rollout Readiness Checker

A small Python command-line tool that turns site readiness assessments into a consistent report. Built for this project management toolkit to demonstrate how delivery governance can be supported by code.

## Run

Requires Python 3.10 or newer. No third-party packages.

From this folder:

```bash
python readiness.py examples/sites.csv
python readiness.py examples/sites.csv --json
python -m unittest -v
```

Example output:

```text
Pilot A: AMBER — uat=amber
Wave 1 B: RED — Duplicate supplier records
Wave 1 C: GREEN
```

## Input and decision rules

CSV columns: `site,data,uat,training,support,blocker`.

Each readiness check accepts green, amber or red, ignoring capitalization and surrounding spaces. Sites must be nonempty and unique. Leave blocker empty when there is no blocking issue.

- Any blocker or red check makes the site red.
- Otherwise, any amber check makes the site amber.
- A site is green only when all checks are green and no blocker is recorded.

Exit codes: **0** means every site is green; **1** means at least one site needs attention; **2** means invalid input or a file error. JSON output includes each site's source checks and blocker.

## Practical use

Maintain the CSV during readiness reviews, run the report before the go/no-go meeting, and use the result to identify sites requiring follow-up. The tool applies the entered assessments; evidence review and launch approval remain responsibilities of the project team.

See the [multi-site rollout playbook](../../06-Multi-Site-Delivery/Multi-Site-ERP-COTS-Rollout-Playbook.md) for accountability, decision gates and hypercare guidance.

Sample data is fictional. This tool does not connect to ERP platforms or contain employer data.
