# WaiverPro Compliance Agent

## Overview

The WaiverPro Compliance Agent is an AI-assisted compliance auditing system that automatically verifies whether the live WaiverPro web application conforms to its official user guidelines.

The system ingests guideline documentation, extracts live UI states from the authenticated application, compares both sources using Retrieval-Augmented Generation (RAG) and Gemini 2.5 Flash, and generates structured compliance reports with supporting evidence.

This project was completed as part of the AI Engineer Internship assignment.

---

## Objectives

The assignment required an automated system capable of:

1. Parsing the WaiverPro User Guidelines PDF.
2. Extracting authenticated UI states from the live application.
3. Comparing live UI behavior against documented requirements.
4. Identifying compliance gaps.
5. Producing structured audit reports with evidence.

---

## Architecture

PDF Guidelines
↓
PyMuPDF
↓
Guideline Text Extraction
↓
Rule Extraction
↓
rules.json
↓
ChromaDB Vector Store
↓
RAG Retrieval
↓
Gemini 2.5 Flash Comparator
↑
Playwright UI Extraction
↑
Live WaiverPro Application
↓
Compliance Reports

---

## Assignment Requirement Mapping

| Requirement | Status |
|------------|------------|
| PDF Guideline Parsing | Complete |
| Authenticated UI Extraction | Complete |
| Dynamic Content Capture | Complete |
| RAG Retrieval | Complete |
| AI Comparison Agent | Complete |
| Compliance Reporting | Complete |
| Screenshot Evidence | Complete |
| Canonical Schema | Complete |
| Coverage Reporting | Complete |

## Technology Choices

### Playwright

Chosen because:

* Handles modern JavaScript-heavy applications.
* Supports authentication flows.
* Captures fully rendered UI states.
* Provides reliable screenshot generation.

Alternatives considered:

* Selenium
* BeautifulSoup
* Requests + HTML parsing

Tradeoff:

Playwright is heavier but significantly more reliable for dynamic web applications.

---

### PyMuPDF

Chosen because:

* Fast PDF text extraction.
* Minimal setup.
* Reliable page-level processing.

Alternatives considered:

* pdfplumber
* pypdf

---

### ChromaDB

Chosen because:

* Lightweight local vector database.
* Easy integration with Python.
* Suitable for small document collections.

Alternatives considered:

* FAISS
* Pinecone

---

### Gemini 2.5 Flash

Chosen because:

* Strong reasoning capability.
* Cost-effective.
* Fast response time.

Used for:

* Guideline interpretation
* UI compliance evaluation
* Discrepancy explanation generation

---

## Pipeline

### Stage 1 – Guideline Ingestion

Input:

* waiverpro_guidelines.pdf

Output:

* guideline_text.txt
* rules.json

Process:

* Extract PDF text using PyMuPDF.
* Split document into guideline sections.
* Store structured rules.

---

### Stage 2 – UI Extraction

Input:

* Live WaiverPro application

Authentication:

* [admin@gmail.com](mailto:admin@gmail.com)
* password

Output:

* Structured JSON UI snapshots
* Screenshots

Captured:

* Headings
* Sections
* Buttons
* Links
* Tables
* Inputs
* Textareas
* Pagination
* Expandable content
* Canonical UI components

---

### Stage 3 – Retrieval

Input:

* Page title

Process:

* Retrieve most relevant guideline section using ChromaDB.

Output:

* Guideline reference
* Guideline text

---

### Stage 4 – AI Compliance Analysis

Input:

* Retrieved guideline
* Extracted UI data

Process:

* Gemini evaluates compliance.
* Produces structured reasoning.

Output:

* Compliance decision
* Discrepancy explanation

---

### Stage 5 – Reporting

Generated artifacts:

* ai_discrepancy_report.json
* ai_compliance_report.md


Reports include:

* Page URL
* Guideline reference
* Compliance status
* Screenshot path
* Timestamp
* AI explanation

---

## Canonical Schema

Each extracted component follows a normalized structure:

```json
{
  "component_type": "button",
  "component_selector": "button",
  "actual_text_content": "Save Changes",
  "retrieved_at": "2026-06-12T08:00:00Z"
}
```

Compliance results contain:

```json
{
  "page_url": "/dashboard/settings",
  "guideline_reference": "Settings",
  "discrepancy_flag": false,
  "discrepancy_reason": "Requirements satisfied",
  "screenshot_path": "data/screenshots/settings.png",
  "retrieved_at": "2026-06-12T08:00:00Z"
}
```

---

## Coverage

Pages analyzed:

* My Applications
* Facilities
* Action Items
* User Management
* Announcements
* FAQs
* Tickets
* Contact
* Settings

Total Pages: 9

---

## Known Limitations

1. Dynamic interactions are sampled rather than exhaustively explored.
2. Backend behavior is not validated.
3. Compliance decisions are AI-assisted and should be reviewed manually.
4. Accessibility extraction depends on browser support.
5. Visual differences are evaluated using extracted evidence rather than pixel-perfect screenshot comparison.

---

## Future Improvements

1. Multi-step interaction coverage.
2. Screenshot-to-guideline visual comparison.
3. Automated route discovery.
4. Historical compliance tracking.
5. Multi-model consensus validation.

---

## Running The Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Extract guidelines:

```bash
python -m app.parser.pdf_parser
python -m app.parser.rule_extractor
```

Extract UI:

```bash
python -m app.extractor.dom_extractor
```

Run AI compliance analysis:

```bash
python -m app.comparator.ai_comparator
```

Generate reports:

```bash
python -m app.report.ai_report_generator
```
