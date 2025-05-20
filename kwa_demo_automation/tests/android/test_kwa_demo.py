import pytest
from kwa_demo_automation.framework.utilities.common import Common
from kwa_demo_automation.framework.utilities.custom_logger import Logger
from kwa_demo_automation.framework.pages.home_page import HomePage

from kwa_demo_automation.framework.utilities.screenshot_utils import get_screenshot_path

log = Logger(file_id=__name__.rsplit(".", 1)[1])

@pytest.mark.kwa_demo
class TestKWADemo:
    """
    Test cases for C2L Application
    """

    #@pytest.mark.skip
    def test_kwa_demo_enter_some_value(self, driver, request, testdata):
        """
        Test #01 : Verify 'ENTER SOME VALUE' functionality.
        Steps:
        01) Click on the 'ENTER SOME VALUE' button.
        """

        test_name = request.node.name.rsplit("[", 1)[0]
        screenshot_path = get_screenshot_path(test_name)
        self.driver = driver

        # Libraries needed
        common = Common(self.driver, testdata)

        # Pages needed
        self.homepage = HomePage(self.driver)

        try:
            log.info(50 * '*')
            log.info("Test #01 : Verify 'ENTER SOME VALUE' functionality.")
            log.info(50 * '*')

            log.info("STEP 01: Click on the 'ENTER SOME VALUE' button.")
            self.homepage.click_enter_some_value_btn()
            log.info("Test #01 :  Verify 'ENTER SOME VALUE' functionality. - Passed")
        except Exception as e:
            self.driver.save_screenshot(screenshot_path)
            log.error(f"Error: {e}")
            log.info("Test #01 :  Verify 'ENTER SOME VALUE' functionality. - Failed")
            raise

    # @pytest.mark.skip
    def test_kwa_demo_contact_us_form(self, driver, request, testdata):
        """
        Test #01 : Verify 'CONTACT US FORM' functionality.
        Steps:
        01) Click on the 'CONTACT US FORM' button.
        """

        test_name = request.node.name.rsplit("[", 1)[0]
        screenshot_path = get_screenshot_path(test_name)
        self.driver = driver

        # Libraries needed
        common = Common(self.driver, testdata)

        # Pages needed
        self.homepage = HomePage(self.driver)

        try:
            log.info(50 * '*')
            log.info("Test #01 : Verify 'CONTACT US FORM' functionality.")
            log.info(50 * '*')

            log.info("STEP 01: Click on the 'CONTACT US FORM' button.")
            self.homepage.click_contact_us_form_btn()
            log.info("Test #01 :  Verify 'CONTACT US FORM' functionality. - Passed")
        except Exception as e:
            self.driver.save_screenshot(screenshot_path)
            log.error(f"Error: {e}")
            log.info("Test #01 :  Verify 'CONTACT US FORM' functionality. - Failed")
            raise
