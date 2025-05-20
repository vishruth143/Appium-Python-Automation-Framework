from appium.webdriver.common.appiumby import AppiumBy
from kwa_demo_automation.framework.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class ContactUsFormPage(BasePage):
    # ------------------------------------------------------------------------------------------------------------------
    #                                                  Element locators
    # ------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------Input Fields---------------------------------------------------
    _enter_name_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Et2")
    _enter_email_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Et3")
    _enter_address_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Et6")
    _enter_mobile_no_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Et7")


    # -----------------------------------------------------Buttons------------------------------------------------------
    _submit_btn = (AppiumBy.ID, "com.code2lead.kwad:id/Btn2")

    # ------------------------------------------------------Texts-------------------------------------------------------
    _name_result_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Tv2")
    _email_result_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Tv7")
    _address_result_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Tv5")
    _mobile_no_result_txt = (AppiumBy.ID, "com.code2lead.kwad:id/Tv6")



    # ------------------------------------------------------------------------------------------------------------------
    #                                                      Elements
    # ------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------Input Fields---------------------------------------------------
    @property
    def enter_name_txt(self, text):
        return self.find_element(*self._enter_name_txt, ec.presence_of_element_located)

    @property
    def enter_email_txt(self, text):
        return self.find_element(*self._enter_email_txt, ec.presence_of_element_located)

    @property
    def enter_address_txt(self, text):
        return self.find_element(*self._enter_address_txt, ec.presence_of_element_located)

    @property
    def enter_mobile_no_txt(self, text):
        return self.find_element(*self._enter_mobile_no_txt, ec.presence_of_element_located)

    # -----------------------------------------------------Buttons------------------------------------------------------
    @property
    def submit_btn(self):
        return self.find_element(*self._submit_btn, ec.element_to_be_clickable)

    # -----------------------------------------------------texts--------------------------------------------------------
    @property
    def name_result_txt(self):
        return self.find_element(*self._name_result_txt, ec.visibility_of_element_located)

    @property
    def email_result_txt(self):
        return self.find_element(*self._email_result_txt, ec.visibility_of_element_located)

    @property
    def address_result_txt(self):
        return self.find_element(*self._address_result_txt, ec.visibility_of_element_located)

    @property
    def phone_no_result_txt(self):
        return self.find_element(*self._mobile_no_result_txt, ec.visibility_of_element_located)

    # ------------------------------------------------------------------------------------------------------------------
    #                                                      Actions
    # ------------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------Is Visible---------------------------------------------------


    # -----------------------------------------------------Enter/Type---------------------------------------------------
    def type_name_txt(self, text):
        self.type_text(*self._enter_name_txt, text)

    def type_email_txt(self, text):
        self.type_text(*self._enter_email_txt, text)

    def type_address_txt(self, text):
        self.type_text(*self._enter_address_txt, text)

    def type_mobile_no_txt(self, text):
        self.type_text(*self._enter_mobile_no_txt, text)


    # -------------------------------------------------------Click------------------------------------------------------
    def click_submit_btn(self):
        self.click(*self._submit_btn)

    # ------------------------------------------------------Get text----------------------------------------------------
    def get_name_result_txt(self):
        return self.get_text(*self._name_result_txt)

    def get_email_result_txt(self):
        return self.get_text(*self._email_result_txt)

    def get_address_result_txt(self):
        return self.get_text(*self._address_result_txt)

    def get_mobile_no_result_txt(self):
        return self.get_text(*self._mobile_no_result_txt)
