from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/contact-us-2/')
title=driver.title
print(title)

country_dropdown=driver.find_element_by_id('Form_submitForm_Country')
select_dropdown=Select(country_dropdown)
select_dropdown.select_by_value('India')

