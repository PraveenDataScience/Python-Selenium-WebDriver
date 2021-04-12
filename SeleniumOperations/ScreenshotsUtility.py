from selenium import webdriver

driver=webdriver.Chrome(executable_path="../SeleniumOperations/drivers/chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.maximize_window()
driver.implicitly_wait(5)

#driver.save_screenshot("C:\\Users\\pande\\Downloads\\chromedriver_win32 (1)\\home.png")
#driver.get_screenshot_as_png("C:\\Users\\pande\\Downloads\\chromedriver_win32 (1)\\ratan")

driver.get_screenshot_as_file("C:\\Users\\pande\\Downloads\\chromedriver_win32 (1)\\home4.png")