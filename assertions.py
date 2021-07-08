import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class HomePagetest(unittest.TestCase):

    def setUp(self):
        #para Linux
        #self.driver = webdriver.Chrome(executable_path='/mnt/c/Users/jm_yg/Dropbox/Educación/MOOCS/selenium/chromedriver.exe')

        #para Windows
        self.driver = webdriver.Chrome(executable_path= r'C:\Users\jm_yg\Dropbox\Educación\MOOCS\selenium\chromedriver.exe')

        driver = self.driver
        driver.get("http://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_element_by_tag_name('img')
        self.assertEqual(3, len(banners))
        
        
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity= 2)