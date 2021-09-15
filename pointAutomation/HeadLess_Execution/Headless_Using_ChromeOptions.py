from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.headless=True

driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.reddit.com/")
title=driver.title
print(title)