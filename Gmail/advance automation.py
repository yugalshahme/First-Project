import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class gmail(unittest.TestCase):

    @classmethod
    def test_setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://gmail.com")

    def test_login_gmail(self, email, password):
        self.driver.find_element_by_id('identifierId').send_keys('testloggly001@gmail.com').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name('Passwd').send_keys('@Yug123@' + Keys.ENTER)

    def test_forgot_password_link(self):
        self.get_pass_link = self.driver.find_element_by_link_text("Forgot password?")
        self.get_pass_link.click()
        self.enter_password = self.driver.find_element_by_id("password")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()