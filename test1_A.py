from playwright.sync_api import sync_playwright

def test_run():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://playwright.dev/python/")
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

        # --- reszta ---
        page.get_by_role("link", name="Community").click()
        page.get_by_role("link", name="Playwright logo Playwright").click()
        page.get_by_role("link", name="Get started").click()

        context.close()
        browser.close()