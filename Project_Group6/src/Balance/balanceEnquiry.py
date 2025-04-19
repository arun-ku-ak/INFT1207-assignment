import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
class TestGuru99:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://demo.guru99.com/V4/")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618854")
        self.driver.find_element(By.NAME, "password").send_keys("umugEjA")
        self.driver.find_element(By.NAME, "btnLogin").click()

    def teardown_method(self):
        self.driver.quit()

    def navigate_to_balance_enquiry(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        balance_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Balance Enquiry"))
        )
        self.driver.execute_script("arguments[0].click();", balance_link)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "accountno"))
        )

    def test_case1(self):
        self.navigate_to_balance_enquiry()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Account Number must not be blank" in body_text

    def test_case2(self):
        self.navigate_to_balance_enquiry()
        self.driver.find_element(By.NAME, "accountno").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case3(self):
        self.navigate_to_balance_enquiry()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case4(self):
        self.navigate_to_balance_enquiry()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case5(self):
        self.navigate_to_balance_enquiry()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case6(self):
        self.navigate_to_balance_enquiry()
        self.driver.find_element(By.NAME, "accountno").send_keys("1221211121")
        time.sleep(1)
        self.driver.find_element(By.NAME, "res").click()
        time.sleep(1)
        accountno_value = self.driver.find_element(By.NAME, "accountno").get_attribute("value")
        assert accountno_value == "", "Account number is reset"

    def test_case7(self):
        self.navigate_to_balance_enquiry()
        self.driver.find_element(By.NAME, "accountno").send_keys("12345623")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert "Account does not exist" in alert.text
        time.sleep(2)
        alert.accept()
