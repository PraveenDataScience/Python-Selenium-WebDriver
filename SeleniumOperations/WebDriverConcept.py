import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
print(driver.title)

driver.find_element(By.CSS_SELECTOR,"input[name='q']").send_keys("Naveen automationlabs")

optionList=driver.find_elements(By.CSS_SELECTOR,"ul.erkvQe li span")
print(len(optionList))

for ele in optionList:
    print(ele.text)
    if ele.text=='naveen automationlabs youtube':
        ele.click()
        break

time.sleep(5)
print("Currrent Page Title is: ",driver.title)
#driver.quit()