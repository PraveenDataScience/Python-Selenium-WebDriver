from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get('https://www.reddit.com/')
driver.maximize_window()

cookie_list = driver.get_cookies()

for cookies in cookie_list:
    print(cookies)