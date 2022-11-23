import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.co.in/")

driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Amazon")
driver.find_element(By.NAME,'q').send_keys(Keys.ENTER)


print(driver.title)
time.sleep(8)
