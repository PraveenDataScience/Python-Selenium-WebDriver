import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''This class is parent of all class'''
"""This Base class contains common methods & utility for all pages """

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()
