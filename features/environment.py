import selenium.webdriver.chrome.service
import selenium.webdriver.firefox.service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from App.application import Application


def browser_init(context, browser: str, headless: str) -> None:
    """
    :param context: Behave context
    :param browser:
    :param headless:
    """
    if browser == "Chrome":
        driver_path: str = ChromeDriverManager().install()
        service: selenium.webdriver.chrome.service.Service = webdriver.ChromeService(driver_path)
        options: Options = webdriver.ChromeOptions()

        if headless == 'True':
            options.add_argument("headless=new")

        context.driver = webdriver.Chrome(
            options=options,
            service=service
        )
    elif browser == "Firefox":
        driver_path: str = GeckoDriverManager().install()
        service: selenium.webdriver.firefox.service.Service = webdriver.FirefoxService(driver_path)
        context.driver = webdriver.Firefox(service=service)

    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 60)
    context.app = Application(context.driver)


def before_scenario(context, scenario) -> None:
    print('\nStarted scenario: ', scenario.name)


def before_step(context, step) -> None:
    print('\nStarted step: ', step)


def after_step(context, step) -> None:
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature) -> None:
    context.driver.delete_all_cookies()
    context.driver.quit()
