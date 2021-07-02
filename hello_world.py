import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    def setUp(self):
        #hay que modificar la ruta rependiendo del sistema operativo y donde esté instalado en chromedriver
        self.driver = webdriver.Chrome(executable_path= r'C:\Users\jm_yg\Dropbox\Educación\MOOCS\selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)


    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reports', report_name= 'Hello World report', ))
