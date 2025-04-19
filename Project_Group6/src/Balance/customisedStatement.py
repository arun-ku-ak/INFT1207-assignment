import time
from telnetlib import EC
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

    def navigate_to_customised_statement(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        balance_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Customised Statement"))
        )
        self.driver.execute_script("arguments[0].click();", balance_link)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "accountno"))
        )

    def test_case1(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "AccSubmit").click()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Account Number must not be blank" in body_text

    def test_case2(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "accountno").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case3(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case4(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case5(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text


    def test_case6(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").click()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "From Date Field must not be blank" in body_text
        time.sleep(1)

    def test_case7(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").click()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "To Date Field must not be blank" in body_text
        time.sleep(1)

    def test_case8(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("121da")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case9(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case10(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("121 213")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case11(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case12(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("123ACC")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case13(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("123!@#")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Special characters are not allowed" in body_text

    def test_case14(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("123 12")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case15(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "numtransaction").send_keys(" ")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Characters are not allowed" in body_text

    def test_case16(self):
        self.navigate_to_customised_statement()
        self.driver.find_element(By.NAME, "accountno").send_keys("1221211121")
        time.sleep(1)

        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2022-02-22")

        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2025-02-22")

        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("10000")

        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("1199")
        time.sleep(1)

        self.driver.find_element(By.NAME, "res").click()
        time.sleep(1)
        accountno_value = self.driver.find_element(By.NAME, "accountno").get_attribute("value")
        assert accountno_value == "", "Account number is reset"

        fdate_value = self.driver.find_element(By.NAME, "fdate").get_attribute("value")
        assert fdate_value == "", "From Date is reset"

        tdate_value = self.driver.find_element(By.NAME, "tdate").get_attribute("value")
        assert tdate_value == "", "To Date is reset"

        amountlowerlimit_value = self.driver.find_element(By.NAME, "amountlowerlimit").get_attribute("value")
        assert amountlowerlimit_value == "", "Minimum Tansaction is reset"

        numtransaction_value = self.driver.find_element(By.NAME, "numtransaction").get_attribute("value")
        assert numtransaction_value == "", "Number of Transaction is reset"


