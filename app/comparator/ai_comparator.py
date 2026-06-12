import json
from pathlib import Path

from app.comparator.gemini_comparator import ask_gemini


RULES_FILE = "data/guidelines/rules.json"
UI_DIR = "data/extracted_ui"
OUTPUT_FILE = "data/reports/ai_discrepancy_report.json"


def load_json(path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    rules = load_json(RULES_FILE)

    results = []

    for file in Path(UI_DIR).glob("*.json"):

        ui_data = load_json(file)

        page_name = (
            file.stem
            .replace("-", " ")
            .replace("_", " ")
            .lower()
        )

        for rule in rules:

            if page_name in rule["title"].lower():

                response = ask_gemini(
                    rule["content"],
                    ui_data
                )

                results.append({
                    "page": rule["title"],
                    "rule": rule["content"],
                    "compliant": response["compliant"],
                    "reason": response["reason"]
                })

                print(
                    f"Checked: {rule['title']} -> {response['compliant']}"
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

        json.dump(
            results,
            f,
            indent=2
        )

    print(
        f"\nSaved AI report -> {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()