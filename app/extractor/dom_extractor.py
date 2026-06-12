
from playwright.sync_api import sync_playwright
import json
import os

URL = "https://white-cliff-0bca3ed00.1.azurestaticapps.net/"
EMAIL = "admin@gmail.com"
PASSWORD = "password"


def login(page):

    page.goto(URL)

    page.click("text=Getting Started")

    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASSWORD)

    page.click("button")

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(3000)


def extract_inputs(page):

    results = []

    for item in page.locator("input").all():

        try:
            results.append({
                "type": item.get_attribute("type"),
                "name": item.get_attribute("name"),
                "placeholder": item.get_attribute("placeholder"),
                "aria_label": item.get_attribute("aria-label"),
                "value": item.input_value()
            })
        except:
            pass

    return results


def extract_selects(page):

    results = []

    for item in page.locator("select").all():

        try:
            options = []

            for option in item.locator("option").all():

                try:
                    options.append(option.inner_text().strip())
                except:
                    pass

            results.append({
                "name": item.get_attribute("name"),
                "aria_label": item.get_attribute("aria-label"),
                "options": options
            })
        except:
            pass

    return results


def extract_textareas(page):

    results = []

    for item in page.locator("textarea").all():

        try:
            results.append({
                "name": item.get_attribute("name"),
                "placeholder": item.get_attribute("placeholder")
            })
        except:
            pass

    return results


def extract_buttons(page):

    results = []

    for btn in page.locator("button").all():

        try:
            results.append({
                "text": btn.inner_text().strip(),
                "aria_label": btn.get_attribute("aria-label"),
                "title": btn.get_attribute("title")
            })
        except:
            pass

    return results


def extract_links(page):

    results = []

    for link in page.locator("a").all():

        try:
            results.append({
                "text": link.inner_text().strip(),
                "href": link.get_attribute("href")
            })
        except:
            pass

    return results


def extract_tables(page):

    tables = []

    for table in page.locator("table").all():

        try:

            headers = []

            for th in table.locator("th").all():

                try:
                    headers.append(
                        th.inner_text().strip()
                    )
                except:
                    pass

            rows = []

            for tr in table.locator("tbody tr").all():

                try:

                    cells = []

                    for td in tr.locator("td").all():

                        try:
                            cells.append(
                                td.inner_text().strip()
                            )
                        except:
                            pass

                    if cells:
                        rows.append(cells)

                except:
                    pass

            tables.append({
                "headers": headers,
                "rows": rows
            })

        except:
            pass

    return tables


def extract_sections(page):

    sections = []

    try:

        for heading in page.locator(
            "h2,h3,h4"
        ).all():

            try:

                text = heading.inner_text().strip()

                if text and text not in sections:

                    sections.append(text)

            except:
                pass

    except:
        pass

    return sections


def extract_table_links(page):

    links = []

    try:

        for link in page.locator(
            "table a"
        ).all():

            try:

                links.append({
                    "text":
                        link.inner_text().strip(),

                    "href":
                        link.get_attribute("href")
                })

            except:
                pass

    except:
        pass

    return links


def extract_expanded_content(page):

    results = []

    try:

        candidates = page.locator(
            '[data-state="open"]'
        )

        for i in range(
            candidates.count()
        ):

            try:

                text = candidates.nth(i)\
                    .inner_text()\
                    .strip()

                if len(text) > 50:

                    results.append(text)

            except:
                pass

    except:
        pass

    return results


def extract_pagination(page):

    pagination = []

    keywords = [
        "Rows per page",
        "Page ",
        "Next",
        "Previous"
    ]

    text = page.locator("body").inner_text()

    for keyword in keywords:

        if keyword in text:
            pagination.append(keyword)

    return pagination


def detect_expandable_content(page):

    try:

        buttons = page.locator("button")

        if buttons.count() == 0:
            return False

        before = page.locator("body").inner_text()

        buttons.first.click(timeout=1000)

        page.wait_for_timeout(1000)

        after = page.locator("body").inner_text()

        return len(after) > len(before)

    except:
        return False


def extract_accessibility(page):

    try:
        snapshot = page.accessibility.snapshot()
        return snapshot
    except:
        return None

def extract_components(page):

    components = []

    selectors = [
        ("button", "button"),
        ("link", "a"),
        ("input", "input")
    ]

    for component_type, selector in selectors:

        for element in page.locator(selector).all():

            try:

                components.append({
    "component_type": component_type,
    "component_selector": selector,
    "actual_text_content":
        element.inner_text().strip()
        if selector != "input"
        else element.input_value(),

    "retrieved_at":
        page.evaluate(
            "() => new Date().toISOString()"
        )
})

            except:
                pass

    return components



def extract_page(page, route):

    page.goto(URL.rstrip("/") + route)

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(3000)

    headings = page.locator(
        "h1,h2,h3,h4,h5,h6"
    ).all_inner_texts()

    page_text = page.locator(
        "body"
    ).inner_text()

    screenshot_file = (
    "data/screenshots/"
    + route.split("/")[-1]
    + ".png"
)
    

    return {

    "page_url": route,

    "screenshot_path":
        screenshot_file,

    "headings": headings,

    "sections":
        extract_sections(page),

    "buttons":
        extract_buttons(page),

    "links":
        extract_links(page),

    "table_links":
        extract_table_links(page),

    "inputs":
        extract_inputs(page),

    "selects":
        extract_selects(page),

    "textareas":
        extract_textareas(page),

    "tables":
        extract_tables(page),

    "pagination":
        extract_pagination(page),

    "expandable_content_detected":
        detect_expandable_content(page),

    "expanded_content":
        extract_expanded_content(page),

    "components":
        extract_components(page),

    "accessibility_tree":
        extract_accessibility(page),

    "page_text":
        page_text

    
}


def main():

    os.makedirs(
        "data/extracted_ui",
        exist_ok=True
    )

    pages = [
        "/dashboard/my-applications",
        "/dashboard/facilities",
        "/dashboard/action-items",
        "/dashboard/user-management",
        "/dashboard/announcements",
        "/dashboard/faqs",
        "/dashboard/tickets",
        "/dashboard/contact",
        "/dashboard/settings"
    ]

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        login(page)

        for route in pages:

            data = extract_page(
                page,
                route
            )

            filename = (
                route.split("/")[-1]
                + ".json"
            )

            with open(
                f"data/extracted_ui/{filename}",
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    data,
                    f,
                    indent=2,
                    ensure_ascii=False
                )

            print(
                f"Saved {filename}"
            )

        browser.close()


if __name__ == "__main__":
    main()
