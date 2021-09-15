from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

best_seller=driver.find_element(By.LINK_TEXT,"Best Sellers")
driver.execute_script("arguments[0].click()",best_seller)

title=driver.execute_script("return document.title;")
print(title)

driver.execute_script("history.go(0);")
driver.execute_script("alert('VDS TECH LABS!!');")


