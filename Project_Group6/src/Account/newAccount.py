import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
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
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        time.sleep(1)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Customer ID is required" in body_text


    def test_case2(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case3(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case4(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case5(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case6(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Current']").click()

    def test_case7(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()

        dropdown = Select(self.driver.find_element(By.NAME, "selaccount"))
        dropdown.select_by_visible_text("Savings")

        selected_option = dropdown.first_selected_option.text
        assert selected_option == "Savings", "'Savings' to be selected in account type dropdown"

    def test_case8(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()

        dropdown = Select(self.driver.find_element(By.NAME, "selaccount"))
        dropdown.select_by_visible_text("Current")

        selected_option = dropdown.first_selected_option.text
        assert selected_option == "Current", "'Current' to be selected in account type dropdown"

    def test_case9(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case10(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Initial deposit" in body_text

    def test_case11(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case12(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case13(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text


    def test_case14(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123")
        self.driver.find_element(By.NAME, "inideposit").send_keys("23343")
        time.sleep(1)
        self.driver.find_element(By.NAME, "reset").click()
        cusid_value = self.driver.find_element(By.NAME, "cusid").get_attribute("value")
        deposit_value = self.driver.find_element(By.NAME, "inideposit").get_attribute("value")

        assert cusid_value == "", "Customer ID is reset"
        assert deposit_value == "", "Initial Deposit is reset"

    def test_case15(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        dropdown.find_element(By.XPATH, "//option[. = 'Savings']").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("12332")
        self.driver.find_element(By.NAME, "button2").click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert "Customer does not exist" in alert.text
        time.sleep(2)
        alert.accept()


