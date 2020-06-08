import unittest
from selenium import webdriver

class gmail_account_creation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('"C:\Python27\chromedriver.exe"')
        cls.driver.maximize_window()
        cls.driver.get('https://accounts.google.com/SignUp?hl=en')

    def account_activation(self):
        self.first_name = self.driver.find_element_by_id('firstname-placeholder').send_keys('test')
        self.last_name = self.driver.find_element_by_id('Lastname').send_keys('loggly004')
        self.gmail_address = self.driver.find_element_by_id('GmailAddress').send_keys('testloggly004')
        self.password = self.driver.find_element_by_id('Passwd').send_keys('@Yug123@')
        self.repeat_password = self.driver.find_element_by_id('PasswdAgain').send_keys('@Yug123@')
        self.month = self.driver.find_element_by_id(':0').click()
        self.month.send_keys('January')
        self.day = self.driver.find_element_by_id('birthday-placeholder').send_keys('28')
        self.year = self.driver.find_element_by_id('birthyear-placeholder').send_keys('1994')
        self.gender = self.driver.find_element_by_xpath('//*[@id="Gender"]/div').click()
        self.gender.send_keys('Male')
        self.submit = self.driver.find_element_by_id('submitbutton').click()

    @classmethod
    def tearDownClass(cls):
        cls.quit()
