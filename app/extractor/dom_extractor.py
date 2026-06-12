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

    inputs = page.locator("input").all()

    for item in inputs:

        try:
            results.append({
                "type": item.get_attribute("type"),
                "name": item.get_attribute("name"),
                "placeholder": item.get_attribute("placeholder"),
                "aria_label": item.get_attribute("aria-label")
            })
        except:
            pass

    return results


def extract_selects(page):

    results = []

    selects = page.locator("select").all()

    for item in selects:

        try:
            results.append({
                "name": item.get_attribute("name"),
                "aria_label": item.get_attribute("aria-label")
            })
        except:
            pass

    return results


def extract_textareas(page):

    results = []

    areas = page.locator("textarea").all()

    for item in areas:

        try:
            results.append({
                "name": item.get_attribute("name"),
                "placeholder": item.get_attribute("placeholder")
            })
        except:
            pass

    return results


def extract_page(page, route):

    page.goto(URL.rstrip("/") + route)

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    headings = page.locator("h1,h2,h3").all_inner_texts()

    buttons = page.locator("button").all_inner_texts()

    links = page.locator("a").all_inner_texts()

    page_text = page.locator("body").inner_text()

    inputs = extract_inputs(page)

    selects = extract_selects(page)

    textareas = extract_textareas(page)

    return {
        "page_url": route,
        "headings": headings,
        "buttons": buttons,
        "links": links,
        "inputs": inputs,
        "selects": selects,
        "textareas": textareas,
        "page_text": page_text
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
                    indent=2
                )

            print(
                f"Saved {filename}"
            )

        browser.close()


if __name__ == "__main__":
    main()