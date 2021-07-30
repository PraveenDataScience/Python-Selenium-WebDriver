from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName='Chrome'

if browserName=='Chrome':
    driver=webdriver.Chrome(ChromeDriverManager().install())
elif browserName=="Firefox":
    driver=webdriver.Firefox(GeckoDriverManager().install())
elif browserName=='Safari':
    driver=webdriver.Safari()
else:
    print("Enter Coorect browser name: " +browserName)

driver.maximize_window()
driver.get("https://www.facebook.com/")
title=driver.title
print(title)

driver.find_element(By.CSS_SELECTOR,'#email').send_keys("VDSTECHLABS@TECH.COM")
driver.find_element(By.CSS_SELECTOR,'#pass').send_keys("awsedrf")
driver.find_element(By.NAME,'login').click()
