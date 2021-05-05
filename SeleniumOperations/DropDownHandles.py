from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()
driver.implicitly_wait(10)

ele_industry=driver.find_element(By.CSS_SELECTOR,'#Form_submitForm_Industry')
select = Select(ele_industry)
select.select_by_visible_text("Education")
