# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob9(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/reports/add_invoice/33/")
        driver.find_element_by_id("contact_name").click()
        driver.find_element_by_id("contact_name").clear()
        driver.find_element_by_id("contact_name").send_keys("Testing 1")
        driver.find_element_by_name("description[]").click()
        driver.find_element_by_name("description[]").clear()
        driver.find_element_by_name("description[]").send_keys("Test item")
        driver.find_element_by_name("price[]").click()
        driver.find_element_by_name("price[]").clear()
        driver.find_element_by_name("price[]").send_keys("50")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='$50.00'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td/input").click()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td/input").clear()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td/input").send_keys("3")
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td[2]/input").click()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td[2]/input").click()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td[2]/input").clear()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td[2]/input").send_keys("Test item2")
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td[3]/input").click()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td[3]/input").clear()
        driver.find_element_by_xpath("//table[@id='invoiceTable']/tbody/tr[2]/td[3]/input").send_keys("15")
        driver.find_element_by_id("tax").click()
        driver.find_element_by_id("tax").clear()
        driver.find_element_by_id("tax").send_keys("10")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Tax:'])[1]/following::button[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
