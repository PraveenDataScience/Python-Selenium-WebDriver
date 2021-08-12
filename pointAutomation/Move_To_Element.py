from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/")


#move to Element By ActionChains Class:
add_on=driver.find_element(By.CSS_SELECTOR,'#header-addons')
act_chain=ActionChains(driver)
act_chain.move_to_element(add_on).perform()
