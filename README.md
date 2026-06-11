# WaiverPro Compliance Agent

Assignment submission for AI Engineer Internship.

## Overview

The WaiverPro Compliance Agent automatically compares the WaiverPro User Guidelines PDF against the live WaiverPro web application and identifies potential discrepancies.

The system performs:

1. PDF guideline extraction
2. Rule extraction from documentation
3. UI data extraction using Playwright
4. Rule-to-UI comparison
5. Discrepancy detection
6. Automated report generation

---

## Project Structure

app/

├── parser/

│ ├── pdf_parser.py

│ └── rule_extractor.py

├── extractor/

│ ├── login.py

│ ├── crawler.py

│ └── dom_extractor.py

├── comparator/

│ └── comparator.py

└── report/

└── report_generator.py

data/

├── guidelines/

├── extracted_ui/

├── screenshots/

└── reports/

---

## Workflow

PDF → guideline_text.txt

→ rules.json

→ extracted UI JSON

→ discrepancy comparison

→ discrepancy_report.json

→ final_report.md

---

## Implemented Features

* ✅ PDF Parsing
* ✅ Rule Extraction
* ✅ Playwright Login Automation
* ✅ DOM Extraction
* ✅ UI Screenshot Capture
* ✅ Compliance Comparison Engine
* ✅ Markdown Report Generation

---

## Example Output

* Rules Extracted: 13
* Pages Analyzed: 9
* Discrepancies Detected: 6

---

## Tech Stack

* Python  3.10+
* Playwright
* PyMuPDF
* JSON
* Markdown

---

## Status

Working end-to-end prototype completed.
