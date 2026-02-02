import time

import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_link_playwright_documentation(set_up) -> None:
    page = set_up
    page.wait_for_load_state()
    page.get_by_role("button", name="Accept all").click()
    page.get_by_label("Search", exact=True).click()
    page.goto("https://www.google.com/search?q=playwright")
    page.get_by_text("Playwright: Fast and reliable end-to-end testing for modern").click()
    page.get_by_text("Node.jsNode.jsPythonJava.NET").hover()
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Docs").click()
    (expect(page.get_by_role("link",
                             name="Write tests using web first assertions, page fixtures and locators"))
     .to_be_visible())

    print('TC is finished')
