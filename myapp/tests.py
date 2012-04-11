from django.test import LiveServerTestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        """
        Specify the in-browser testing tool
        """
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MySeleniumTests, cls).tearDownClass()
        cls.selenium.quit()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        name_input = self.selenium.find_element_by_name("name")
        #name_input = self.selenium.find_element(by=By.ID, value="id_name")
        name_input.send_keys('myuser')
        self.selenium.find_element_by_xpath('//button[@value="Submit"]').click()

