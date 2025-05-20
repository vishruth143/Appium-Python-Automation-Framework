from appium.webdriver.webdriver import WebDriver  # Appium WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, by, locator, condition=ec.presence_of_element_located):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                condition((by, locator))
            )
        except TimeoutException as e:
            raise Exception(f"[FIND_ELEMENT] Element not found: ({by}, {locator}) | {str(e)}")

    def find_elements(self, by, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                ec.presence_of_all_elements_located((by, locator))
            )
        except TimeoutException as e:
            raise Exception(f"[FIND_ELEMENTS] Elements not found: ({by}, {locator}) | {str(e)}")

    def is_element_present(self, by, locator):
        try:
            self.driver.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_visible(self, by, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            return False

    def click(self, by, locator):
        try:
            self.find_element(by, locator).click()
        except Exception as e:
            raise Exception(f"[CLICK] Failed to click: ({by}, {locator}) | {str(e)}")

    def type_text(self, by, locator, text):
        try:
            element = self.find_element(by, locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"[TYPE_TEXT] Failed to type text: ({by}, {locator}) | {str(e)}")

    def get_text(self, by, locator):
        try:
            return self.find_element(by, locator).text
        except Exception as e:
            raise Exception(f"[GET_TEXT] Failed to get text: ({by}, {locator}) | {str(e)}")

    def wait_until_not_visible(self, by, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until_not(
                ec.visibility_of_element_located((by, locator))
            )
        except TimeoutException:
            raise Exception(f"[WAIT_UNTIL_NOT_VISIBLE] Element still visible after timeout: ({by}, {locator})")

    def wait_for_clickable(self, by, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                ec.element_to_be_clickable((by, locator))
            )
        except TimeoutException as e:
            raise Exception(f"[WAIT_FOR_CLICKABLE] Element not clickable: ({by}, {locator}) | {str(e)}")