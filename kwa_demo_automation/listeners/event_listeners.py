# pylint: disable=[missing-module-docstring, missing-class-docstring, import-error, missing-function-docstring]
# pylint: disable=[invalid-name, too-few-public-methods, logging-fstring-interpolation, broad-exception-caught]

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from kwa_demo_automation.framework.utilities.custom_logger import Logger
from kwa_demo_automation.framework.utilities.screenshot_utils import get_screenshot_path

log = Logger(file_id=__name__.rsplit(".", 1)[1])

class MyEventListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        print(f"[Event] Navigating to: {url}")
        log.info(f"[Event] Navigating to: {url}")

    def after_navigate_to(self, url, driver):
        print(f"[Event] Navigated to: {url}")
        log.info(f"[Event] Navigated to: {url}")

    def before_find(self, by, value, driver):
        print(f"[Event] Finding element by {by} with value {value}")
        log.info(f"[Event] Finding element by {by} with value {value}")

    def after_find(self, by, value, driver):
        print(f"[Event] Found element by {by} with value {value}")
        log.info(f"[Event] Found element by {by} with value {value}")

    def before_click(self, element, driver):
        print(f"[Event] Clicking on element: {element}")
        log.info(f"[Event] Clicking on element: {element}")

    def after_click(self, element, driver):
        print(f"[Event] Clicked on element: {element}")
        log.info(f"[Event] Clicked on element: {element}")

    def on_exception(self, exception, driver):
        print(f"[Event] Exception occurred: {exception}")
        log.info(f"[Event] Exception occurred: {exception}")
        # Optional: Take screenshot on error
        try:
            test_name = driver.title or "unknown"
            screenshot_path = get_screenshot_path(f"error_{test_name}")
            driver.save_screenshot(screenshot_path)
            print(f"[Event] Screenshot saved to {screenshot_path}")
            log.info(f"[Event] Screenshot saved to {screenshot_path}")
        except Exception as e:
            print(f"[Event] Failed to take screenshot: {e}")
            log.info(f"[Event] Failed to take screenshot: {e}")
