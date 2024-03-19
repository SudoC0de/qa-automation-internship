from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Pages.base_page import Page


class SecondaryListingsPage(Page):
    elements: dict[str, tuple[str, str]] = {
        'FilterListingsButton': (By.CSS_SELECTOR, 'div[wized="openFiltersWindow"]'),
        'ListingCards': (By.CSS_SELECTOR, '.listing-card'),
        'ForSaleCards': (By.XPATH, '//div[text()="For sale"]')
    }

    def verify_secondary_listings_opened(self) -> None:
        self.wait_until_visible(self.elements['FilterListingsButton'])

        assert "secondary" in self.get_url(), "Secondary Listings Page has not opened"

    def click_filter_button(self) -> None:
        self.wait_until_visible(self.elements['FilterListingsButton'])
        self.click(self.elements['FilterListingsButton'])

    def verify_listings_for_sales(self) -> None:
        listings: list[WebElement] = self.find_elements(self.elements['ListingCards'])
        for_sale_listings: list[WebElement] = self.find_elements(self.elements['ForSaleCards'])

        assert len(listings) == len(for_sale_listings), \
            f"Expected {len(for_sale_listings)} for sale listings. Received {len(listings)} instead"
