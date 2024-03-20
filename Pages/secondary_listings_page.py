from time import sleep
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
        self.verify_listings_loaded()

        assert "secondary" in self.get_url(), "Secondary Listings Page has not opened"
        assert len(self.find_elements(self.elements['ForSaleCards'])) > 0, \
            f"Secondary Listings have not loaded after 60 seconds"

    def click_filter_button(self) -> None:
        self.wait_until_visible(self.elements['FilterListingsButton'])
        self.click(self.elements['FilterListingsButton'])

    def verify_listings_for_sales(self) -> None:
        self.verify_listings_loaded()
        listings: list[WebElement] = self.find_elements(self.elements['ListingCards'])
        for_sale_listings: list[WebElement] = self.find_elements(self.elements['ForSaleCards'])

        assert len(listings) == len(for_sale_listings), \
            f"Expected {len(for_sale_listings)} for sale listings. Received {len(listings)} instead"

    def verify_listings_loaded(self) -> None:
        count: int = 0

        # Sometimes the listings are slow to load (despite being present on the DOM) so this sleep was added
        while len(self.find_elements(self.elements['ForSaleCards'])) == 0 and count < 60:
            count += 1
            sleep(1)
