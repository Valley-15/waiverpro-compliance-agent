import json
from pathlib import Path
from datetime import datetime

DISCREPANCY_FILE = "data/reports/ai_discrepancy_report.json"
RULES_FILE = "data/guidelines/rules.json"
OUTPUT_FILE = "data/reports/final_report.md"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    discrepancies = load_json(DISCREPANCY_FILE)
    rules = load_json(RULES_FILE)

    report = []

    report.append("# WaiverPro Compliance Report\n")

    report.append(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    )

    report.append("## Summary\n")

    report.append(
        f"- Rules extracted: {len(rules)}"
    )

    report.append(
        f"- Discrepancies detected: {len(discrepancies)}\n"
    )

    report.append("---\n")

    if not discrepancies:

        report.append(
            "## Result\n\nNo discrepancies detected.\n"
        )

    else:

        report.append("## Discrepancies Found\n")

        grouped = {}

        for item in discrepancies:

            page = item["page"]

            if page not in grouped:
                grouped[page] = []

            grouped[page].append(item["issue"])

        for page, issues in grouped.items():

            report.append(f"\n### {page}\n")

            for issue in issues:
                report.append(f"- {issue}")

    report.append("\n\n---\n")

    report.append("## Notes\n")

    report.append(
        "- This report was generated automatically by the WaiverPro Compliance Agent."
    )

    report.append(
        "- Some discrepancies may be caused by UI extraction limitations."
    )

    report.append(
        "- Manual verification is recommended for final compliance review."
    )

    Path("data/reports").mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("\n".join(report))

    print(f"Report saved -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()