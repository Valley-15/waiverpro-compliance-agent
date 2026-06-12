from app.comparator.gemini_comparator import ask_gemini

rule = """
The announcements page should provide search functionality.
"""

ui = {
    "headings": ["Announcements"],
    "page_text": "Announcements Search Introducing Smarter Analytics"
}

result = ask_gemini(rule, ui)

print(result)