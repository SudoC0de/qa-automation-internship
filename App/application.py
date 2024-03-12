from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.base_page import Page
from Pages.main_menu_page import MainMenuPage
from Pages.secondary_listings_page import SecondaryListingsPage
from Pages.secondary_listings_sidebar_page import SecondaryListingsSidebarPage
from Pages.signin_page import SigninPage


class Application:
    def __init__(self, driver: WebDriver):
        self.pages: Page = Page(driver)
        self.main_menu_page: MainMenuPage = MainMenuPage(driver)
        self.secondary_listings_page: SecondaryListingsPage = SecondaryListingsPage(driver)
        self.secondary_listings_sidebar_page: SecondaryListingsSidebarPage = SecondaryListingsSidebarPage(driver)
        self.signin_page: SigninPage = SigninPage(driver)
