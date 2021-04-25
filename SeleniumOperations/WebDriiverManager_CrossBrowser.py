from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName="chrome"

if browserName=="chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName=="firefox":
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName=="safari":
    driver=webdriver.safari()

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://app.hubspot.com/login")

time.sleep(5)

driver.find_element(By.ID,'username').send_keys('praveen.seleniumautomation@gmail.com')
driver.find_element(By.ID,'password').send_keys('Test@321654')
driver.find_element(By.ID,'loginBtn').click()

print(driver.title)
time.sleep(3)
driver.quit()


