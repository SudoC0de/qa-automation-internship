from typing import List
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Support.logger import logger


class Page:
    def __init__(self, driver: WebDriver) -> None:
        logger.info("Initializing Page Components")
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

    def open(self, url: str) -> None:
        logger.info(f'Opening url: {url}')
        self.driver.get(url)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple[str, str]) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple[str, str]) -> None:
        logger.info(f'Clicking element: {locator}')
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_element(self, element: WebElement) -> None:
        logger.info(f'Element clicking element: {element}')
        self.wait.until(EC.element_to_be_clickable(element)).click()

    def script_click(self, locator: tuple[str, str]) -> None:
        logger.info(f'Script clicking element: {locator}')
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click()", self.find_element(locator))

    def action_click(self, locator: tuple[str, str]) -> None:
        logger.info(f'Action Chain clicking element: {locator}')
        self.wait.until(EC.element_to_be_clickable(locator))

        element: WebElement = self.find_element(locator)
        actions: ActionChains = ActionChains(self.driver)

        actions.move_to_element(element).click(element).perform()

    def close_window(self) -> None:
        logger.info(f'Closing Window')
        self.driver.close()

    def enter_text(self, text: str, locator: tuple[str, str]) -> None:
        logger.info(f'Entering text at element: {locator}')

        text_input: WebElement = self.driver.find_element(*locator)

        text_input.clear()
        text_input.send_keys(text)

    def wait_until_located(self, locator: tuple[str, str]) -> None:
        logger.info(f'Waiting until element ({locator}) is located')
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_visible(self, locator: tuple[str, str]) -> None:
        logger.info(f'Waiting until element ({locator}) is visible')
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator: tuple[str, str]) -> None:
        logger.info(f'Waiting until element ({locator}) is invisible')
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_until_clickable(self, locator: tuple[str, str]) -> None:
        logger.info(f'Waiting until element ({locator}) is clickable')
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_new_window_opened(self, num_windows: int) -> None:
        logger.info(f'Waiting until {num_windows} are opened')
        self.wait.until(EC.number_of_windows_to_be(num_windows))

    def get_url(self) -> str:
        logger.info('Getting current url')

        return self.driver.current_url
