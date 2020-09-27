from selenium import webdriver
import time
import pytest


MAIN_URL = 'https://sharelane.com/cgi-bin/main.py'
def browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.quit()

def test_registration(url):

    driver = webdriver.Chrome()
    driver.get(url)
    sign_up = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[3]/td/table/tbody/tr/td[4]/a')
    sign_up.click()
    send_keys = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[5]/td/table/'
                                             'tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')
    send_keys.send_keys('12345')
    cont_button = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                               'tr[2]/td/table/tbody/tr[3]/td[2]/input')
    cont_button.click()
    first_name = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                              'tr[2]/td/table/tbody/tr[1]/td[2]/input')
    first_name.send_keys('Alex')
    email = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                         'tr[2]/td/table/tbody/tr[3]/td[2]/input')
    email.send_keys('zhe.depotop@gmail.com')
    password = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                            'tr[2]/td/table/tbody/tr[4]/td[2]/input')
    password.send_keys('33160900')
    conf_password = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[5]/td/table/tbody/'
                                                 'tr[2]/td/table/tbody/tr[5]/td[2]/input')
    conf_password.send_keys('33160900')
    buttom_reg = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[5]/td/table/'
                                              'tbody/tr[2]/td/table/tbody/tr[6]/td[2]/input')
    buttom_reg.click()

    message = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[4]/td/span').text
    ass_email = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[6]/td/table/tbody/'
                                             'tr[4]/td/table/tbody/tr[1]/td[2]/b').text
    ass_pass = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[6]/td/table/tbody/'
                                            'tr[4]/td/table/tbody/tr[2]/td[2]').text
    assert message == 'Account is created!', 'FAIL'
    assert len(ass_email) > 0, 'FAIL'
    assert len(ass_pass) > 0, 'FAIL'

    time.sleep(3)
    driver.quit()

def main():
    test_registration(MAIN_URL)


if __name__ == '__main__':
    main()
