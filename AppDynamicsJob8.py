# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob8(unittest.TestCase):
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
        driver.find_element_by_xpath("//div[@id='calendar']/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[2]/td[3]/div/div[2]/div/a/div/div/div[2]/div").click()
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/jobs/jobs/60")
        driver.find_element_by_link_text("Mark as In Progress").click()
        driver.find_element_by_link_text("Mark as Completed").click()
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/reports/submit/60/")
        driver.find_element_by_id("id_job_details").click()
        driver.find_element_by_id("id_job_details").clear()
        driver.find_element_by_id("id_job_details").send_keys("Finished job, this is a test report of all details")
        driver.find_element_by_id("id_job_issues").click()
        driver.find_element_by_id("id_job_issues").clear()
        driver.find_element_by_id("id_job_issues").send_keys("no issues")
        driver.find_element_by_id("id_payment_method").click()
        Select(driver.find_element_by_id("id_payment_method")).select_by_visible_text("Card")
        driver.find_element_by_id("id_payment_received").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Additional image:'])[1]/following::button[1]").click()
        driver.get("http://ec2-3-14-11-53.us-east-2.compute.amazonaws.com:8000/reports/add_invoice/33/")
    
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
