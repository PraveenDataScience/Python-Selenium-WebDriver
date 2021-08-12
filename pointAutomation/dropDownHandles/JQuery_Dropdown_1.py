from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(5)
driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(5)
list_drp=driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')

for ld in list_drp:
    print(ld.text)
    if(ld.text == 'choice 2 2'):
        ld.click()
        break




