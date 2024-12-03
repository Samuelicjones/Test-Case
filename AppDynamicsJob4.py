# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob4(unittest.TestCase):
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
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/teams/team-dashboard/example-team-name/")
        driver.find_element_by_link_text("Customers").click()
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/customers/customers/")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Test Customer")
        driver.find_element_by_id("id_email").click()
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("Test@email.com")
        driver.find_element_by_id("id_phone_number").click()
        driver.find_element_by_id("id_phone_number").clear()
        driver.find_element_by_id("id_phone_number").send_keys("123-456-7890")
        driver.find_element_by_id("id_company").click()
        driver.find_element_by_id("id_company").clear()
        driver.find_element_by_id("id_company").send_keys("Test Company")
        driver.find_element_by_id("id_address").click()
        driver.find_element_by_id("id_address").clear()
        driver.find_element_by_id("id_address").send_keys("Test Ave 123")
        driver.find_element_by_id("id_notes").click()
        driver.find_element_by_id("id_notes").clear()
        driver.find_element_by_id("id_notes").send_keys("This is a test.")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::button[1]").click()
    
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
