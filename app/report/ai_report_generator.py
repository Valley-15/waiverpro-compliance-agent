import json
from pathlib import Path
from datetime import datetime

AI_REPORT_FILE = "data/reports/ai_discrepancy_report.json"
OUTPUT_FILE = "data/reports/ai_compliance_report.md"


def load_json(path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    results = load_json(AI_REPORT_FILE)

    total_pages = len(results)

    compliant_count = sum(
        1 for r in results
        if r["compliant"]
    )

    non_compliant_count = (
        total_pages - compliant_count
    )

    pass_rate = round(
        (compliant_count / total_pages) * 100,
        2
    ) if total_pages > 0 else 0

    report = []

    report.append(
        "# WaiverPro AI Compliance Report\n"
    )

    report.append(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    )

    report.append("## Summary\n")

    report.append(
        f"- Pages Checked: {total_pages}"
    )

    report.append(
        f"- Compliant Pages: {compliant_count}"
    )

    report.append(
        f"- Needs Review: {non_compliant_count}"
    )

    report.append(
        f"- Pass Rate: {pass_rate}%\n"
    )

    report.append("---\n")

    report.append(
        "## Detailed Results\n"
    )

    for item in results:

        status = (
            "✅ PASS"
            if item["compliant"]
            else "❌ REVIEW"
        )

        report.append(
            f"\n### {item['page_file']}"
        )

        report.append(
            f"- Status: {status}"
        )

        report.append(
            f"- Retrieved Rule: {item['retrieved_rule']}"
        )

        report.append(
            f"- Reason: {item['reason']}"
        )

    report.append("\n---\n")

    report.append("## Notes\n")

    report.append(
        "- Analysis performed using Gemini 2.5 Flash via OpenRouter."
    )

    report.append(
        "- Relevant guideline sections retrieved using ChromaDB."
    )

    report.append(
        "- Results should be manually reviewed before compliance decisions."
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

    print(
        f"AI report saved -> {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()