import time
import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Customer ID is required" in body_text

    def test_case2(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case3(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case4(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case5(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_6(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert alert.text == "Do you really want to delete this Customer?"
        alert.accept()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert alert.text == "Customer does not exist!!"
        alert.accept()




