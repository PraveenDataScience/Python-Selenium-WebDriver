from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

best_seller=driver.find_element(By.LINK_TEXT,'Best Sellers')

title=driver.execute_script("return document.title;")
#print(title)

inner_text=driver.execute_script("return document.documentElement.innerText;")
print(inner_text)
print(title)

driver.execute_script("arguments[0].style.border='3px solid red'",best_seller)
