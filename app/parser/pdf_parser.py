import fitz
from pathlib import Path


PDF_PATH = Path("data/guidelines/waiverpro_guidelines.pdf")
OUTPUT_PATH = Path("data/guidelines/guideline_text.txt")


def extract_pdf_text(pdf_path):
    """
    Extract all text from PDF.
    Returns a single string.
    """

    document = fitz.open(pdf_path)

    full_text = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()

        full_text.append(
            f"\n\n===== PAGE {page_num + 1} =====\n\n{text}"
        )

    document.close()

    return "".join(full_text)


def save_text(text, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    if not PDF_PATH.exists():
        print(f"PDF not found: {PDF_PATH}")
        return

    print("Reading PDF...")

    text = extract_pdf_text(PDF_PATH)

    save_text(text, OUTPUT_PATH)

    print(f"Saved extracted text to: {OUTPUT_PATH}")
    print(f"Characters extracted: {len(text)}")


if __name__ == "__main__":
    main()