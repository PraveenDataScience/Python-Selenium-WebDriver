import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://demo.guru99.com/test/newtours/")

path = "C://Users//pande//PycharmProjects//PytestFramework//PythonDataDrivenTesting//Login1.xlsx"
