from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/contact-us-2/")
print(driver.title)

def select_value(element, value):
    select=Select(element)
    select.select_by_value(value)

emp_ele=driver.find_element_by_id('Form_submitForm_NoOfEmployees')
cont_ele=driver.find_element(By.ID,'Form_submitForm_Country')
select_value(emp_ele,"11 - 15")
select_value(cont_ele,"India")