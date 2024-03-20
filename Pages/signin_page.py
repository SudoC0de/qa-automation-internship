from selenium.webdriver.common.by import By
from Pages.base_page import Page


class SigninPage(Page):
    elements: dict[str, tuple[str, str]] = {
        'EmailInputBox': (By.ID, 'email-2'),
        'PasswordInputBox': (By.ID, 'field'),
        'LoginButton': (By.CSS_SELECTOR, 'a[wized="loginButton"]')
    }

    def open_signin_page(self) -> None:
        self.open("https://soft.reelly.io/sign-in")

    def verify_signin_page_opened(self) -> None:
        self.wait_until_visible(self.elements['EmailInputBox'])

        assert "sign-in" in self.get_url(), "Sign-in page has not been opened"

    def login(self, email: str, password: str) -> None:
        self.wait_until_visible(self.elements['EmailInputBox'])
        self.enter_text(email, self.elements['EmailInputBox'])
        self.enter_text(password, self.elements['PasswordInputBox'])
        self.click(self.elements['LoginButton'])
        self.wait_until_invisible(self.elements['LoginButton'])
