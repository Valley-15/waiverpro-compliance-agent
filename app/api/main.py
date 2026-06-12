from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path
import json

from app.pipeline.audit_runner import run_audit

app = FastAPI(
    title="WaiverPro Compliance Agent",
    version="1.4"
)

templates = Jinja2Templates(
    directory="templates"
)


@app.get("/")
def root():

    return {
        "project": "WaiverPro Compliance Agent",
        "version": "1.4",
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
            "pages_checked": 0,
            "passed": 0,
            "needs_review": 0,
            "pass_rate": 0
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


@app.get("/dashboard")
def dashboard(request: Request):

    summary_data = summary()

    report_file = Path(
        "data/reports/ai_discrepancy_report.json"
    )

    results = []

    if report_file.exists():

        with open(
            report_file,
            "r",
            encoding="utf-8"
        ) as f:

            results = json.load(f)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "summary": summary_data,
            "results": results
        }
    )


@app.post("/run-audit")
def trigger_audit():

    run_audit()

    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )