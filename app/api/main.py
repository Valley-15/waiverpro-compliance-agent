from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI(
    title="WaiverPro Compliance API",
    version="1.3"
)


@app.get("/")
def root():

    return {
        "project": "WaiverPro Compliance Agent",
        "version": "1.3",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/report")
def get_report():

    report_file = Path(
        "data/reports/ai_discrepancy_report.json"
    )

    if not report_file.exists():

        return {
            "error": "Report not found"
        }

    with open(
        report_file,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


@app.get("/summary")
def summary():

    report_file = Path(
        "data/reports/ai_discrepancy_report.json"
    )

    if not report_file.exists():

        return {
            "error": "Report not found"
        }

    with open(
        report_file,
        "r",
        encoding="utf-8"
    ) as f:

        results = json.load(f)

    total = len(results)

    passed = sum(
        1 for r in results
        if r["compliant"]
    )

    failed = total - passed

    pass_rate = round(
        (passed / total) * 100,
        2
    ) if total else 0

    return {
        "pages_checked": total,
        "passed": passed,
        "needs_review": failed,
        "pass_rate": pass_rate
    }