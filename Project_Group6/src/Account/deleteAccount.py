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

    def teardown_method(self, method):
        self.driver.quit()

    def test_case1(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Account Number must not be blank" in body_text


    def test_case2(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case3(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case4(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case5(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text


    def test_case6(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1221211121")
        time.sleep(1)
        self.driver.find_element(By.NAME, "res").click()
        time.sleep(1)
        accountno_value = self.driver.find_element(By.NAME, "accountno").get_attribute("value")
        assert accountno_value == "", "Account number is reset"

    def test_7(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123456")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert alert.text == "Do you really want to delete this Account?"
        alert.accept()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert alert.text == "Account does not exist"
        alert.accept()




