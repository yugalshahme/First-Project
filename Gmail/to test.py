import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class phplogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.set_window_size(1000,1000)
        cls.driver.get("http://www.phptravels.net/")

    def test_to_check_lang_dropdown(self):
        try:
            self.element = self.driver.find_element_by_xpath('//*[@id="currency"]')
            self.all_options = self.element.find_elements_by_tag_name("option")
            for option in self.all_options:
                print("Value is: %s" % option.get_attribute("value"))
                option.click()
        except NoSuchElementException:
            print False
        print True

    def test_dropdown(self):
        try:
            self.select = Select(self.driver.find_element_by_xpath('//*[@id="currency"]'))
            self.all_selected_options = self.select.all_selected_options
            print True
        except NoSuchElementException:
            print False


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

