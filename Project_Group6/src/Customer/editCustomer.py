import time
from telnetlib import EC

from selenium.webdriver import Keys
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

    def submit_customer_id(self, customer_id="31830"):
        # This is the reusable method we’ll call from each test case
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "cusid"))
        )
        self.driver.find_element(By.NAME, "cusid").send_keys(customer_id)
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)

    def test_case1(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Customer ID is required" in body_text

    def test_case2(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case3(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case4(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case5(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case6(self):
        self.submit_customer_id()
        addr_field = self.driver.find_element(By.NAME, "addr")
        addr_field.clear()
        addr_field.send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Address Field must not be blank" in body_text

    def test_case7(self):
        self.submit_customer_id()
        city_field = self.driver.find_element(By.NAME, "city")
        city_field.clear()
        city_field.send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "City Field must not be blank" in body_text

    def test_case8(self):
        self.submit_customer_id()
        city_field = self.driver.find_element(By.NAME, "city")
        city_field.clear()
        city_field.send_keys("1234acc")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Numbers are not allowed" in body_text

    def test_case9(self):
        self.submit_customer_id()
        city_field = self.driver.find_element(By.NAME, "city")
        city_field.clear()
        city_field.send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case10(self):
        self.submit_customer_id()
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.clear()
        state_field.send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "State must not be blank" in body_text

    def test_case11(self):
        self.submit_customer_id()
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.clear()
        state_field.send_keys("1234acc")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Numbers are not allowed" in body_text

    def test_case12(self):
        self.submit_customer_id()
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.clear()
        state_field.send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case13(self):
        self.submit_customer_id()
        state_field = self.driver.find_element(By.NAME, "state")
        state_field.clear()
        state_field.send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case14(self):
        self.submit_customer_id()
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.clear()
        pin_field.send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case15(self):
        self.submit_customer_id()
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.clear()
        pin_field.send_keys("1234acc")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case16(self):
        self.submit_customer_id()
        pin_field = self.driver.find_element(By.NAME, "pinno")
        pin_field.clear()
        pin_field.send_keys("1235")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "PIN Code must have 6 Digits" in body_text

    def test_case17(self):
        self.submit_customer_id()
        phone_field = self.driver.find_element(By.NAME, "telephoneno")
        phone_field.clear()
        phone_field.send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Mobile no must not be blank" in body_text

    def test_case18(self):
        self.submit_customer_id()
        phone_field = self.driver.find_element(By.NAME, "telephoneno")
        phone_field.clear()
        phone_field.send_keys("123 122")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case19(self):
        self.submit_customer_id()
        phone_field = self.driver.find_element(By.NAME, "telephoneno")
        phone_field.clear()
        phone_field.send_keys("364268@#277")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case20(self):
        self.submit_customer_id()
        email_field = self.driver.find_element(By.NAME, "emailid")
        email_field.clear()
        email_field.send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Email-ID must not be blank" in body_text

    def test_case21(self):
        self.submit_customer_id()
        email_field = self.driver.find_element(By.NAME, "emailid")
        email_field.clear()
        email_field.send_keys("guru99@gmail.")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Email-ID is not valid" in body_text








