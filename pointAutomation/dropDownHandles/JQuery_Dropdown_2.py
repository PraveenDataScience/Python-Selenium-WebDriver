from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def list_value(drop_down, value):
    for Id in drop_down:
        print(Id.text)
        if(Id.text==value):
            Id.click()
            break;


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element(By.ID,"justAnInputBox").click()
time.sleep(5)
list_drp=driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
list_value(list_drp,'choice 2 2' )
list_value(list_drp,'choice 2 1' )
list_value(list_drp,'choice 1' )