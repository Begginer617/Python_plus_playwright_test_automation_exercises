import re
from playwright.sync_api import sync_playwright, expect


def test_run1():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1500)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.google.com/")
        page.wait_for_url("https://www.google.com/")
        page.goto("https://playwright.dev/python/")
        page.pause()

        page.get_by_role("link", name="Docs").click()
        page.get_by_role("link", name="API", exact=True).click()

        page.get_by_role("button", name="Python").hover()
        page.get_by_role("link", name="Java").click()

        page.get_by_role("button", name="Java").hover()
        page.get_by_role("link", name=".NET").click()

        page.get_by_role("button", name=".NET").hover()
        page.get_by_role("link", name="Node.js").click()

        page.get_by_role("button", name="Node.js").hover()
        page.get_by_role("link", name="Python").click()

        page.get_by_role("link", name="Community").click()
        page.get_by_role("link", name="Playwright logo Playwright").click()
        page.get_by_role("link", name="Get started").click()

        print("TC skonczony")

        context.close()
        browser.close()


def test_run2():
    with (sync_playwright() as playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://playwright.dev/")
        expect(page.get_by_role("navigation", name="Main")).to_be_visible()

        page.get_by_role("link", name="Docs").click()
        expect(page.get_by_role("navigation", name="Docs sidebar")).to_be_visible()

        page.get_by_role("link", name="How to install Playwright").click()
        page.get_by_role("link", name="Writing tests", exact=True).click()
        expect(page.get_by_role("heading", name="First testDirect link to")).to_be_visible()

        page.get_by_role("link", name="How to write the first test").click()
        page.get_by_role("code").filter(
            has_text=re.compile(r"^await expect\(page\)\.toHaveTitle\(/Playwright\/\);$")
        ).click()

        context.close()
        browser.close()