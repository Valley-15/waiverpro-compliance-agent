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

    page.wait_for_timeout(3000)


def extract_page(page, route):

    page.goto(URL.rstrip("/") + route)

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    headings = page.locator("h1,h2,h3").all_inner_texts()

    buttons = page.locator("button").all_inner_texts()

    links = page.locator("a").all_inner_texts()

    texts = page.locator("body").inner_text()

    return {
        "page_url": route,
        "headings": headings,
        "buttons": buttons,
        "links": links,
        "page_text": texts
    }


def main():

    os.makedirs("data/extracted_ui", exist_ok=True)

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

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        login(page)

        for route in pages:

            data = extract_page(page, route)

            filename = route.split("/")[-1] + ".json"

            with open(
                f"data/extracted_ui/{filename}",
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(data, f, indent=2)

            print(f"Saved {filename}")

        browser.close()


if __name__ == "__main__":
    main()