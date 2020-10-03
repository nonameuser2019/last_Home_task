from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class ShareSearchLocators:
    LOCATOR_SIGNUP_BUTTON = (By.XPATH, '/html/body/center/table/tbody/tr[3]/td/table/tbody/tr/td[4]/a')
    LOCATOR_ZIP_CODE_INPUT = (By.XPATH, '/html/body/center/table/tbody/tr[5]/td/table/'
                                             'tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')
    LOCATRO_ZIP_SEND_BUTTON = (By.XPATH, '/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                               'tr[2]/td/table/tbody/tr[3]/td[2]/input')
    LOCATOR_FIRST_NAME = (By.XPATH, '/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                              'tr[2]/td/table/tbody/tr[1]/td[2]/input')
    LOCATOR_EMAIL = (By.XPATH, '/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                         'tr[2]/td/table/tbody/tr[3]/td[2]/input')
    LOCATOR_PASSWORD = (By.XPATH, '/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                            'tr[2]/td/table/tbody/tr[4]/td[2]/input')
    LOCATOR_CONF_PASS = (By.XPATH, '/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                                 'tr[2]/td/table/tbody/tr[5]/td[2]/input')
    LOCATOR_REG_BUTTON = (By.XPATH, '/html/body/center/table/tbody/tr[5]/td/table/'
                                              'tbody/tr[2]/td/table/tbody/tr[6]/td[2]/input')
    LOCATOR_1_MESSAGE = (By.XPATH, '/html/body/center/table/tbody/tr[4]/td/span')
    LOCATOR_2_MESSAGE = (By.XPATH, '/html/body/center/table/tbody/tr[6]/td/table/tbody/'
                                             'tr[4]/td/table/tbody/tr[1]/td[2]/b')
    LOCATOR_3_MESSAGE = (By.XPATH, '/html/body/center/table/tbody/tr[6]/td/table/tbody/'
                                            'tr[4]/td/table/tbody/tr[2]/td[2]')


class RegisterHelp(BasePage):
    def enter_signup(self):
        sign_up_button = self.find_element(ShareSearchLocators.LOCATOR_SIGNUP_BUTTON)
        sign_up_button.click()


    def enter_zip_code(self):
        zip_code_inp = self.find_element(ShareSearchLocators.LOCATOR_ZIP_CODE_INPUT)
        zip_code_inp.send_keys('12345')
        zip_code_button = self.find_element(ShareSearchLocators.LOCATRO_ZIP_SEND_BUTTON)
        zip_code_button.click()


    def filling_out_reg_form(self):
        first_name_field = self.find_element(ShareSearchLocators.LOCATOR_FIRST_NAME)
        first_name_field.send_keys('Alex')
        email_field = self.find_element(ShareSearchLocators.LOCATOR_EMAIL)
        email_field.send_keys('zhe.depotop@gmail.com')
        pas_field = self.find_element(ShareSearchLocators.LOCATOR_PASSWORD)
        pas_field.send_keys('33160900')
        conf_pass_field = self.find_element(ShareSearchLocators.LOCATOR_CONF_PASS)
        conf_pass_field.send_keys('33160900')
        reg_button = self.find_element(ShareSearchLocators.LOCATOR_REG_BUTTON)
        reg_button.click()
        time.sleep(3)
        reg_message = self.find_element(ShareSearchLocators.LOCATOR_1_MESSAGE).text
        reg_message2 = self.find_element(ShareSearchLocators.LOCATOR_2_MESSAGE).text
        reg_message3 = self.find_element(ShareSearchLocators.LOCATOR_3_MESSAGE).text
        return reg_message, reg_message2, reg_message3




