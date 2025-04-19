import time
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys

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
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Customer name must not be blank" in body_text

    def test_case2(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("1234acc")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Numbers are not allowed" in body_text

    def test_case3(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case4(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case5(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Address Field must not be blank" in body_text


    def test_case6(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case7(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "City Field must not be blank" in body_text

    def test_case8(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case9(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("1234acc")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Numbers are not allowed" in body_text

    def test_case10(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case11(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "State must not be blank" in body_text

    def test_case12(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("1234acc")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Numbers are not allowed" in body_text

    def test_case13(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case14(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case15(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text


    def test_case16(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case17(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234acc")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case18(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("1235")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "PIN Code must have 6 Digits" in body_text

    def test_case19(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys()
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "PIN Code must not be blank" in body_text

    def test_case20(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case21(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("123 122")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case22(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("364268@#277")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case23(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Mobile no must not be blank" in body_text

    def test_case24(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys()
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Email-ID must not be blank" in body_text

    def test_case25(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "First character can not have space" in body_text

    def test_case26(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail.")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Email-ID is not valid" in body_text







