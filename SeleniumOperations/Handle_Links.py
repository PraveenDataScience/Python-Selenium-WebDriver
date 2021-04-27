from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.implicitly_wait(5)

links=driver.find_elements(By.TAG_NAME,"a")
print("No of Links: ",len(links))

#Print text of All Links:
for link in links:
    print(link.text)

# Click on link based on LINK_TEXT & PARTIAL_LINK_TEXT
#driver.find_element(By.LINK_TEXT,"SUPPORT").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"SUPP").click()
print(driver.title)