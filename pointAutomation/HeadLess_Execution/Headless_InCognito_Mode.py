from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.headless=False
options.add_argument("--incognito")

driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com/")

title=driver.title
print(title)