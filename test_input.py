import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


#@pytest.mark.xfail(reason="strona nie jest dostępna")
def test_input(playwright: Playwright) -> None:

    # Wybór przeglądarki (w tym przypadku - chromium)
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)

    # Otwarcie nowej karty w przeglądarce
    page = browser.new_page()

    # Nawigacja do strony the-internet.herokuapp.com
    page.goto("http://the-internet.herokuapp.com/inputs")

    # Wybranie inputu
    page.get_by_role("spinbutton").click()

    # Wprowadzenie danych w postaci liczb w pole inputu
    page.get_by_role("spinbutton").fill("01234")

    # Sprawdzenie wysłanych danych do inputu
    expect(page.get_by_role("spinbutton")).not_to_be_visible()

    # Zamknięcie przeglądarki
    browser.close()


def test_input_2(playwright: Playwright) -> None:

    # Wybór przeglądarki (w tym przypadku - chromium)
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)

    # Otwarcie nowej karty w przeglądarce
    page = browser.new_page()

    # Nawigacja do strony the-internet.herokuapp.com
    page.goto("http://the-internet.herokuapp.com/inputs")

    # Wybranie inputu
    page.get_by_role("spinbutton").click()

    # Wprowadzenie danych w postaci liczb w pole inputu
    page.get_by_role("spinbutton").fill("01234")

    # Sprawdzenie wysłanych danych do inputu
    expect(page.get_by_role("spinbutton")).not_to_be_empty()

    # Zamknięcie przeglądarki
    browser.close()