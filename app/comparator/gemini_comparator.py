import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "google/gemini-2.5-flash"


def ask_gemini(rule_text, ui_data):

    prompt = f"""
You are a QA compliance auditor.

Guideline Requirement:

{rule_text}

Extracted UI Data:

{json.dumps(ui_data, indent=2)}

Instructions:

1. Compare the guideline against the extracted UI.
2. Use ONLY evidence present in the extracted UI.
3. Do NOT assume functionality that is not shown.
4. Do NOT fail a page because evidence is represented differently than the guideline wording.
5. If equivalent evidence exists, mark compliant=true.
6. Missing minor implementation details should not cause failure when the main requirement is clearly satisfied.
7. Be consistent and practical.

Return ONLY valid JSON:

{{
  "compliant": true,
  "reason": "short explanation"
}}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    response.raise_for_status()

    result = response.json()

    content = result["choices"][0]["message"]["content"]

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        return json.loads(content)

    except Exception:

        return {
            "compliant": False,
            "reason": f"Unable to parse model response: {content}"
        }