"""Assess ERP/COTS site readiness from a CSV file. Python 3.10+, no dependencies."""
import argparse
import csv
import json
import sys

CHECKS = ("data", "uat", "training", "support")
VALID = {"green", "amber", "red"}

def assess(path):
    results = []
    with open(path, newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        required = {"site", "blocker", *CHECKS}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Missing columns: " + ", ".join(sorted(required - set(reader.fieldnames or []))))
        seen = set()
        for line, row in enumerate(reader, start=2):
            site = (row.get("site") or "").strip()
            if not site or site.casefold() in seen:
                raise ValueError(f"Line {line}: site must be nonempty and unique")
            seen.add(site.casefold())
            checks = {key: (row.get(key) or "").strip().lower() for key in CHECKS}
            if any(value not in VALID for value in checks.values()):
                raise ValueError(f"Line {line}: readiness values must be green, amber or red")
            blocker = (row.get("blocker") or "").strip()
            status = "red" if blocker or "red" in checks.values() else (
                "amber" if "amber" in checks.values() else "green")
            results.append({"site": site, "status": status, "checks": checks, "blocker": blocker})
    if not results:
        raise ValueError("The input must contain at least one site")
    return results

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="CSV with site, data, uat, training, support, blocker")
    parser.add_argument("--json", action="store_true", help="Print structured JSON")
    args = parser.parse_args()
    try:
        results = assess(args.csv_file)
    except (OSError, ValueError, csv.Error) as error:
        print(f"Input error: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"sites": results}, indent=2))
    else:
        for item in results:
            reason = item["blocker"] or ", ".join(
                f"{key}={value}" for key, value in item["checks"].items() if value != "green")
            print(f'{item["site"]}: {item["status"].upper()}' + (f" — {reason}" if reason else ""))
    return 1 if any(item["status"] != "green" for item in results) else 0

if __name__ == "__main__":
    sys.exit(main())
