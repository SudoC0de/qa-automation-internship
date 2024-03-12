from selenium.webdriver.common.by import By
from Pages.base_page import Page


class SecondaryListingsSidebarPage(Page):
    elements: dict[str, tuple[str, str]] = {
        'SidebarTitle': (By.CSS_SELECTOR, 'div.filters-title-wrapper > .h1-filters'),
        'SellListingTypeSelection': (By.CSS_SELECTOR, 'div[wized="ListingTypeSell"]'),
        'ApplyFilterButton': (By.CSS_SELECTOR, 'a[wized="applyFilterButtonMLS"]'),
        'CloseSidebarButton': (By.CSS_SELECTOR, '.close-filters-window')
    }

    def wait_until_secondary_listings_sidebar_opened(self) -> None:
        self.wait_until_visible(self.elements['SidebarTitle'])

    def filter_listings_by_sell(self) -> None:
        self.click(self.elements['SellListingTypeSelection'])
        self.click(self.elements['ApplyFilterButton'])
        self.wait_until_invisible(self.elements['SidebarTitle'])
