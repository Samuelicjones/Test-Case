# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob6(unittest.TestCase):
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
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/customers/customers/")
        driver.find_element_by_link_text("Jobs").click()
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/jobs/jobs/")
        driver.find_element_by_id("id_customer").click()
        Select(driver.find_element_by_id("id_customer")).select_by_visible_text("Test Customer")
        driver.find_element_by_id("id_team_member").click()
        Select(driver.find_element_by_id("id_team_member")).select_by_visible_text("Test16")
        driver.find_element_by_id("id_start_time").click()
        driver.find_element_by_id("id_start_time").clear()
        driver.find_element_by_id("id_start_time").send_keys("2024-12-10T23:03")
        driver.find_element_by_id("id_priority").click()
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("Low")
        driver.find_element_by_id("id_job_description").click()
        driver.find_element_by_id("id_job_description").clear()
        driver.find_element_by_id("id_job_description").send_keys("This is a test job for Test Customer")
        driver.find_element_by_id("id_additional_notes").click()
        driver.find_element_by_id("id_additional_notes").clear()
        driver.find_element_by_id("id_additional_notes").send_keys("No notes")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Additional notes:'])[1]/following::button[1]").click()
    
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
