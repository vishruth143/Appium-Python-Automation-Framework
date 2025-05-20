from appium.webdriver.common.appiumby import AppiumBy
from kwa_demo_automation.framework.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class EnterSomeValuePage(BasePage):
    # ------------------------------------------------------------------------------------------------------------------
    #                                                  Element locators
    # ------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------Input Fields---------------------------------------------------
    _enter_some_value_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Et1")

    # -----------------------------------------------------Buttons------------------------------------------------------
    _submit_btn = (AppiumBy.ID, "com.code2lead.kwad:id/Btn1")

    # ------------------------------------------------------Texts-------------------------------------------------------
    _result_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Tv1")



    # ------------------------------------------------------------------------------------------------------------------
    #                                                      Elements
    # ------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------Input Fields---------------------------------------------------
    @property
    def enter_some_value_txt(self):
        return self.find_element(*self._enter_some_value_txt, ec.presence_of_element_located)

    # -----------------------------------------------------Buttons------------------------------------------------------
    @property
    def submit_btn(self):
        return self.find_element(*self._submit_btn, ec.element_to_be_clickable)

    # -----------------------------------------------------texts--------------------------------------------------------
    @property
    def result_txt(self):
        return self.find_element(*self._result_txt, ec.visibility_of_element_located)

    # ------------------------------------------------------------------------------------------------------------------
    #                                                      Actions
    # ------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------Is Visible---------------------------------------------------


    # -----------------------------------------------------Enter/Type---------------------------------------------------
    def type_enter_some_value_txt(self, text):
        self.type_text(*self._enter_some_value_txt, text)


    # -------------------------------------------------------Click------------------------------------------------------
    def click_submit_btn(self):
        self.click(*self._submit_btn)

    # ------------------------------------------------------Get text----------------------------------------------------
    def get_result_txt(self):
        return self.get_text(*self._result_txt)