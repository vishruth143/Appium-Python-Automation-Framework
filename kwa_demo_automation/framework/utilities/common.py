# pylint: disable=[line-too-long, missing-module-docstring, missing-module-docstring, missing-function-docstring]
# pylint: disable=[unused-variable, missing-class-docstring]

import time
import random
from datetime import datetime, timezone
import shutil

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

from faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from kwa_demo_automation.config.config_parser import ConfigParser

class Common:
    @staticmethod
    def fake_name():
        return Faker().name()

    @staticmethod
    def fake_first_name():
        return Faker().first_name()

    @staticmethod
    def fake_last_name():
        return Faker().last_name()

    @staticmethod
    def fake_ssn():
        return Faker().ssn().replace('-', '')

    @staticmethod
    def fake_phonenumber():
        return str(random.randint(2220000000, 2229999999))

    @staticmethod
    def get_date():
        return datetime.now(timezone.utc).strftime('%m-%d-%Y')

    # Copy
    @staticmethod
    def copy(driver: WebDriver):
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    @staticmethod
    def enter(driver: WebDriver):
        ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    @staticmethod
    def tab(driver: WebDriver):
        ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()

    # Paste
    @staticmethod
    def paste(driver: WebDriver):
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    @staticmethod
    def select_all(driver: WebDriver):
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    @staticmethod
    def delete(driver: WebDriver):
        ActionChains(driver).key_down(Keys.DELETE).key_up(Keys.DELETE).perform()

    # Scroll web page up by pressing Ctrl+Home
    @staticmethod
    def scroll_up(driver: WebDriver):
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.HOME).key_up(Keys.HOME).key_up(
            Keys.CONTROL).perform()

    # Scroll web page down by pressing Ctrl+End
    @staticmethod
    def scroll_down(driver: WebDriver):
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.END).key_up(Keys.END).key_up(
            Keys.CONTROL).perform()

    # Scroll for web element to view
    @staticmethod
    def scroll_into_view(driver: WebDriver, element: WebElement):
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

    # Move to web element
    @staticmethod
    def move_to_element(driver: WebDriver, element: WebElement):
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

    def __init__(self, driver=None, test_data=None):
        self.driver = driver
        self.test_data = test_data
        self.pta_login_url, self.pta_login_username, self.pta_login_password = "", "", ""

        common_config = ConfigParser.load_config("common_config")

        # Pages needed


def wait_for_an_element(driver, timeout, poll_frequency, element_locator):
    """Wait for the specified element to be present on the page.

    Args:
        driver (WebDriver): The webdriver instance to use.
        timeout (int): The maximum amount of time to wait in seconds.
        poll_frequency (int): The frequency at which to check for the element in seconds.
        element_locator (tuple): The locator for the element, in the format (By.TYPE, 'value').
    """
    WebDriverWait(driver, timeout, poll_frequency).until(ec.presence_of_element_located(element_locator))

def generic_wait(driver, timeout):
    wait = WebDriverWait(driver, timeout)

    # Wait for timeout
    wait.until(lambda driver: driver.execute_script("return true;"), "Timeout")

def wait_for_element_to_disappear(driver, element_locator, timeout=60):
    try:
        element_present = ec.presence_of_element_located(element_locator)
        WebDriverWait(driver, timeout).until_not(element_present)
    except TimeoutError:
        print("Timed out waiting for element to disappear")

def save_excel(sheet_name, df, input_path, output_path):
    shutil.copy(input_path, output_path)

    with pd.ExcelWriter(output_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Post-process green fill for "Pass" in "Status"
    wb = load_workbook(output_path)
    ws = wb["PTA"]

    # Define fills
    green_fill = PatternFill(fill_type="solid", fgColor="90EE90") # light green
    red_fill = PatternFill(fill_type="solid", fgColor="FF7F7F")  # light red

    # Find 'Status' column index (1-based)
    status_col_index = [cell.value for cell in ws[1]].index("Status") + 1  # 1-based index

    # Apply color based on status value
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        cell = row[status_col_index - 1]
        if cell.value == 'Pass':
            cell.fill = green_fill
        elif cell.value == 'Fail':
            cell.fill = red_fill

    # Save changes
    wb.save(output_path)
