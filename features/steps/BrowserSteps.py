import features.environment
from behave import given, when, then


@given('Start {browser}. Headless = {headless}')
def start_browser(context, browser: str, headless: str) -> None:
    features.environment.browser_init(context, browser, headless)
