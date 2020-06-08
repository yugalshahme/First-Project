import unittest
from selenium import webdriver

class gmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://gmail.com")

    def Login(self):
        self.email = self.driver.find_element_by_id("identifierId")
        self.email.send_keys("testloggly001@gmail.com")
        self.next_button = self.driver.find_element_by_link_text("Next")
        self.next_button.click()
        self.driver.implicitly_wait(5)
        self.password = self.driver.find_elements_by_name("password")
        self.password.send_keys("@Yug123@")
        self.click_next = self.driver.find_elements_by_link_text("Next")

    def forgot_password_link(self):
        self.get_pass_link = self.driver.find_element_by_link_text("Forgot password?")
        self.get_pass_link.click()
        self.enter_password = self.driver.find_element_by_id("password")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()