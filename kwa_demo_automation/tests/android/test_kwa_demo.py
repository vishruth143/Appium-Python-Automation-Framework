import pytest
from kwa_demo_automation.framework.utilities.common import Common
from kwa_demo_automation.framework.utilities.custom_logger import Logger
from kwa_demo_automation.framework.pages.home_page import HomePage
from kwa_demo_automation.framework.pages.enter_some_value_page import EnterSomeValuePage
from kwa_demo_automation.framework.pages.contact_us_form_page import ContactUsFormPage

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
        02) Type 'ENTER SOME VALUE'.
        03) Click on 'SUBMIT' button.
        04) Verify entered text.
        """

        test_name = request.node.name.rsplit("[", 1)[0]
        screenshot_path = get_screenshot_path(test_name)
        self.driver = driver

        # Libraries needed
        common = Common(self.driver, testdata)

        # Pages needed
        self.homepage = HomePage(self.driver)
        self.entersomevaluepage = EnterSomeValuePage(self.driver)

        try:
            log.info(50 * '*')
            log.info("Test #01 : Verify 'ENTER SOME VALUE' functionality.")
            log.info(50 * '*')

            log.info("STEP 01: Click on the 'ENTER SOME VALUE' button.")
            self.homepage.click_enter_some_value_btn()
            log.info("STEP 02: Type 'ENTER SOME VALUE'.")
            text = testdata[test_name]['text']
            self.entersomevaluepage.type_enter_some_value_txt(text)
            log.info("STEP 03: Click on the 'SUBMIT' button.")
            self.entersomevaluepage.click_submit_btn()
            log.info("STEP 04: Verify entered text.")
            if self.entersomevaluepage.get_result_txt()==text:
                log.info("Test #01 :  Verify 'ENTER SOME VALUE' functionality. - Passed")
            else:
                self.driver.save_screenshot(screenshot_path)
                log.info("Test #01 :  Verify 'ENTER SOME VALUE' functionality. - Failed")
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
        02) Enter 'Name'.
        03) Enter 'Email'.
        04) Enter 'Address'.
        05) Enter 'Mobile No'.
        06) Click on 'SUBMIT'.
        07) Verify entered text.
        """

        test_name = request.node.name.rsplit("[", 1)[0]
        screenshot_path = get_screenshot_path(test_name)
        self.driver = driver

        # Libraries needed
        common = Common(self.driver, testdata)

        # Pages needed
        self.homepage = HomePage(self.driver)
        self.contactusformpage = ContactUsFormPage(self.driver)

        try:
            log.info(50 * '*')
            log.info("Test #01 : Verify 'CONTACT US FORM' functionality.")
            log.info(50 * '*')

            log.info("STEP 01: Click on the 'CONTACT US FORM' button.")
            self.homepage.click_contact_us_form_btn()
            log.info("STEP 02: Enter 'Name'.")
            self.contactusformpage.type_name_txt(testdata[test_name]['Name'])
            log.info("STEP 03: Enter 'Email'.")
            self.contactusformpage.type_email_txt(testdata[test_name]['Email'])
            log.info("STEP 04: Enter 'Address'.")
            self.contactusformpage.type_address_txt(testdata[test_name]['Address'])
            log.info("STEP 05: Enter 'Mobile No'.")
            self.contactusformpage.type_mobile_no_txt(testdata[test_name]['Mobile No'])
            log.info("STEP 06: Click on the 'SUBMIT' button.")
            self.contactusformpage.click_submit_btn()
            log.info("STEP 07: Verify entered text.")
            if (testdata[test_name]['Name']==self.contactusformpage.get_name_result_txt().split(":")[1].strip() and
                    testdata[test_name]['Email']==self.contactusformpage.get_email_result_txt().split(":")[1].strip() and
                    testdata[test_name]['Address']==self.contactusformpage.get_address_result_txt().split(":")[1].strip() and
                    str(testdata[test_name]['Mobile No'])==self.contactusformpage.get_mobile_no_result_txt().split(":")[1].strip()):
                log.info("Test #01 :  Verify 'CONTACT US FORM' functionality. - Passed")
            else:
                log.info("Test #01 :  Verify 'CONTACT US FORM' functionality. - Failed")
        except Exception as e:
            self.driver.save_screenshot(screenshot_path)
            log.error(f"Error: {e}")
            log.info("Test #01 :  Verify 'CONTACT US FORM' functionality. - Failed")
            raise
