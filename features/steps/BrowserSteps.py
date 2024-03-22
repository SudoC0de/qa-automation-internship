import features.environment
from behave import given, when, then


@given('Start {browser}. Headless = {headless}, Remote = {remote}, RemoteOS = {remote_os}, RemoteOSVer = {remote_os_ver}')
def start_browser(context, browser: str, headless: str, remote: str, remote_os: str, remote_os_ver: str) -> None:
    features.environment.browser_init(context, browser, headless, remote, remote_os, remote_os_ver)
