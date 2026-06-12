import json
from pathlib import Path

from app.comparator.gemini_comparator import ask_gemini
from app.rag.retriever import retrieve_rule


UI_DIR = "data/extracted_ui"
OUTPUT_FILE = "data/reports/ai_discrepancy_report.json"


def load_json(path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    results = []

    for file in Path(UI_DIR).glob("*.json"):

        ui_data = load_json(file)

        page_title = ""

        if ui_data.get("headings"):
            page_title = ui_data["headings"][0]

        query = page_title

        retrieval = retrieve_rule(
            query,
            top_k=1
        )

        rule_text = retrieval["documents"][0][0]

        rule_title = retrieval["metadatas"][0][0]["title"]

        response = ask_gemini(
            rule_text,
            ui_data
        )

        results.append({
            "page_file": file.name,
            "retrieved_rule": rule_title,
            "compliant": response["compliant"],
            "reason": response["reason"]
        })

        print(
            f"Checked: {file.stem} -> {rule_title} -> {response['compliant']}"
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