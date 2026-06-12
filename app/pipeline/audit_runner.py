import subprocess
import sys
from pathlib import Path


def run_audit():

    print("\nSTEP 1: Extracting UI...")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "app.extractor.dom_extractor"
        ],
        check=True
    )

    print("\nSTEP 2: Running AI comparison...")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "app.comparator.ai_comparator"
        ],
        check=True
    )

    print("\nSTEP 3: Generating report...")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "app.report.ai_report_generator"
        ],
        check=True
    )

    report_file = Path(
        "data/reports/ai_compliance_report.md"
    )

    return {
        "status": "success",
        "report_exists": report_file.exists(),
        "report_path": str(report_file)
    }


if __name__ == "__main__":

    result = run_audit()

    print("\nAUDIT COMPLETE")

    print(result)