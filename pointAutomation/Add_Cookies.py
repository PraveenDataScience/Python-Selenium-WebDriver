from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get("https://reddit.com/")
driver.maximize_window()

cookie_list=driver.get_cookies()

for cookies in cookie_list:
    print(cookies)

driver.add_cookie({"name":"Praveen","domain":"reddit.com","value":"Mishra"})

cookie_list=driver.get_cookies()

#print("============================")
for cookies in cookie_list:
    print(cookies)
