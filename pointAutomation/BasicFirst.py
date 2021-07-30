from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.facebook.com/")
title=driver.title
print(title)
driver.close()
