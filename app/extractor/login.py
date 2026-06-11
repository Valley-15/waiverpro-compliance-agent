from playwright.sync_api import sync_playwright


URL = "https://white-cliff-0bca3ed00.1.azurestaticapps.net/"
EMAIL = "admin@gmail.com"
PASSWORD = "password"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(URL)

        page.click("text=Getting Started")

        page.fill('input[type="email"]', EMAIL)

        page.fill('input[type="password"]', PASSWORD)

        page.click("button")

        page.wait_for_timeout(5000)

        page.screenshot(
            path="data/screenshots/dashboard_after_login.png",
            full_page=True
        )

        print("Login successful screenshot saved")

        browser.close()


if __name__ == "__main__":
    main()