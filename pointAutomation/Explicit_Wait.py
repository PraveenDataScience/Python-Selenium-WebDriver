from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(ChromeDriverManager().install())

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element  after explicitly waiting for 10 seconds
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Courses")))

element.click()
