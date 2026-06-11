from playwright.sync_api import sync_playwright
import os

URL = "https://white-cliff-0bca3ed00.1.azurestaticapps.net/"
EMAIL = "admin@gmail.com"
PASSWORD = "password"

PAGES = [
    ("my-applications", "/dashboard/my-applications"),
    ("facilities", "/dashboard/facilities"),
    ("action-items", "/dashboard/action-items"),
    ("user-management", "/dashboard/user-management"),
    ("announcements", "/dashboard/announcements"),
    ("faqs", "/dashboard/faqs"),
    ("tickets", "/dashboard/tickets"),
    ("contact", "/dashboard/contact"),
    ("settings", "/dashboard/settings"),
]


def login(page):
    page.goto(URL)

    page.click("text=Getting Started")

    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASSWORD)

    page.click("button")

    page.wait_for_timeout(3000)


def main():

    os.makedirs("data/screenshots", exist_ok=True)

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        login(page)

        for name, route in PAGES:

            page.goto(URL.rstrip("/") + route)

            page.wait_for_timeout(10000)

            page.screenshot(
                path=f"data/screenshots/{name}.png",
                full_page=True
            )

            print(f"Saved: {name}")

        browser.close()


if __name__ == "__main__":
    main()