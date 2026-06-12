import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "google/gemini-2.5-flash"


def ask_gemini(rule_text, ui_data):

    prompt = f"""
You are a strict QA compliance auditor.

Guideline Requirement:

{rule_text}

Extracted UI Data:

{json.dumps(ui_data, indent=2)}

Instructions:

- Compare the guideline against the extracted UI.
- Only use evidence present in the UI data.
- Do NOT assume missing functionality exists.
- Do NOT infer features that are not explicitly shown.
- If evidence is missing, mark compliant as false.
- Return valid JSON only.

Expected format:

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