from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/contact-us-2/")
print(driver.title)

def select_value(element, value):
    select=Select(element)
    select.select_by_value(value)

emp_ele=driver.find_element_by_id('Form_submitForm_NoOfEmployees')
cont_ele=driver.find_element(By.ID,'Form_submitForm_Country')
select_value(emp_ele,"11 - 15")
select_value(cont_ele,"India")

select=Select(cont_ele)
country_list=select.options
for con in country_list:
    print(con.text)
    if(con.text=='Zambia'):
        con.click()
        break

driver.quit()