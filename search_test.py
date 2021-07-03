import unittest
from selenium import webdriver

class HomePagetest(unittest.TestCase):

    def setUp(self):
        #para Linux
        #self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

        #para Windows
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity= 2)