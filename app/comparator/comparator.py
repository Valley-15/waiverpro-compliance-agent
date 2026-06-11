import json
from pathlib import Path

RULES_FILE = "data/guidelines/rules.json"
UI_DIR = "data/extracted_ui"
OUTPUT_FILE = "data/reports/discrepancy_report.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def flatten_json(obj):
    result = []

    if isinstance(obj, dict):
        for v in obj.values():
            result.extend(flatten_json(v))

    elif isinstance(obj, list):
        for item in obj:
            result.extend(flatten_json(item))

    else:
        result.append(str(obj))

    return result


def has_table(ui_text):
    table_words = [
        "name",
        "status",
        "email",
        "facility",
        "waiver id",
        "created on",
        "actions"
    ]

    matches = sum(
        1 for word in table_words
        if word in ui_text
    )

    return matches >= 2


def has_chart(ui_text):
    chart_words = [
        "applications by type",
        "applications overview",
        "total",
        "high",
        "medium",
        "low"
    ]

    return any(
        word in ui_text
        for word in chart_words
    )


def compare_rule(rule, ui_data):

    discrepancies = []

    ui_text = " ".join(
        flatten_json(ui_data)
    ).lower()

    rule_text = rule["content"].lower()

    checks = {
        "invite": "invite user",
        "search": "search",
        "status": "status",
        "toggle": "toggle",
        "notification": "notification",
    }

    for guide_word, ui_word in checks.items():

        if guide_word in rule_text:

            if ui_word not in ui_text:

                discrepancies.append({
                    "page": rule["title"],
                    "issue": f"{guide_word} mentioned in guide but not found in UI"
                })

    if "table" in rule_text:
        if not has_table(ui_text):
            discrepancies.append({
                "page": rule["title"],
                "issue": "table mentioned in guide but not found in UI"
            })

    if "chart" in rule_text:
        if not has_chart(ui_text):
            discrepancies.append({
                "page": rule["title"],
                "issue": "chart mentioned in guide but not found in UI"
            })

    return discrepancies


def main():

    rules = load_json(RULES_FILE)

    all_discrepancies = []

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

                all_discrepancies.extend(
                    compare_rule(rule, ui_data)
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
            all_discrepancies,
            f,
            indent=2
        )

    print(
        f"Found {len(all_discrepancies)} discrepancies"
    )


if __name__ == "__main__":
    main()