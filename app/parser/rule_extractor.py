import json
import re
from pathlib import Path

GUIDELINE_FILE = Path("data/guidelines/guideline_text.txt")
OUTPUT_FILE = Path("data/guidelines/rules.json")


def extract_sections(text):
    pattern = r"S E C T I O N\s+\d+"
    matches = list(re.finditer(pattern, text))

    sections = []

    for i, match in enumerate(matches):
        start = match.start()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        sections.append(text[start:end])

    return sections


def parse_section(section_text):

    title = "Unknown"
    url = ""

    lines = [
        line.strip()
        for line in section_text.splitlines()
        if line.strip()
    ]

    for i, line in enumerate(lines):

        if line.startswith("URL"):
            url = line.replace("URL", "").strip()

        if (
            i > 0
            and not lines[i - 1].startswith("S E C T I O N")
            and len(line) > 3
        ):
            pass

    for i, line in enumerate(lines):

        if line.startswith("S E C T I O N"):

            if i + 1 < len(lines):
                title = lines[i + 1]
                break

    return {
        "title": title,
        "url": url,
        "content": section_text
    }


def main():

    if not GUIDELINE_FILE.exists():
        print("guideline_text.txt not found")
        return

    text = GUIDELINE_FILE.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    sections = extract_sections(text)

    rules = []

    for section in sections:
        rules.append(parse_section(section))

    OUTPUT_FILE.write_text(
        json.dumps(rules, indent=2),
        encoding="utf-8"
    )

    print(f"Rules extracted: {len(rules)}")
    print(f"Saved -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()