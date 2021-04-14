from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from webdriver_manager.firefox import GeckoDriverManager


option=webdriver.ChromeOptions()
#option.headless=True
option.add_argument("--headless")
driver=webdriver.Chrome(ChromeDriverManager().install(), options=option) 

'''
option=webdriver.FirefoxOptions()
option.headless=True
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=option)
'''

driver.implicitly_wait(10)
driver.get("http://amezon.in")
print(driver.title)


