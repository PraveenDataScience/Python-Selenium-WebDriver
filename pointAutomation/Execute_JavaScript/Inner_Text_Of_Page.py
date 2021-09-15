from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")

mobile_link=driver.find_element_by_link_text("Mobiles")
driver.execute_script("arguments[0].click();",mobile_link)

title=driver.execute_script("return document.title;")
print(title)

inner_text=driver.execute_script("return document.documentElement.innerText;")
print(inner_text)