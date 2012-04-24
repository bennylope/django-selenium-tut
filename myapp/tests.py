from django.test import LiveServerTestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class SeleniumTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SeleniumTestCase, cls).tearDownClass()
        cls.selenium.quit()


class MyAppTests(SeleniumTestCase):

    def test_form(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        username = self.selenium.find_element_by_name('username')
        username.send_keys('bennylope')
        self.selenium.find_element_by_name('submit').click()

    def test_form_validation(self):
        """Validate the form with JavaScript"""
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        first_name = self.selenium.find_element_by_name('first_name')
        first_name.send_keys('ben')
        last_name = self.selenium.find_element_by_name('last_name')
        last_name.send_keys('lopatin')
        self.selenium.find_elements(By.XPATH, "//input[@value='benlopatin']")

