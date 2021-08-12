from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileUpload.html")

file_upload=driver.find_element(By.XPATH,"//input[@id='input-4']")
file_upload.send_keys("C://Users//priya pandey//Downloads//input000.txt")

#driver.execute_script('return document.getElementsByName("Remove")[0].click()')

removeButton=driver.find_element(By.XPATH,"//span[text()='Remove']")
time.sleep(15)
driver.execute_script("arguments[0].click();", removeButton)
#removeButton.click()



