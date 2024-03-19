from selenium.webdriver.common.by import By
from Pages.base_page import Page


class MainMenuPage(Page):
    elements: dict[str, tuple[str, str]] = {
        'SecondaryListingsButton': (By.CSS_SELECTOR, 'a[href="/secondary-listings"] > div > .menu-button-text')
    }

    def open_reelly_homepage(self) -> None:
        self.open("https://soft.reelly.io/")

    def click_secondary_listings_button(self) -> None:
        self.wait_until_visible(self.elements['SecondaryListingsButton'])
        self.click(self.elements['SecondaryListingsButton'])
