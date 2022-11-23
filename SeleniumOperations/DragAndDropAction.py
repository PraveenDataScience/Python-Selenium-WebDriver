from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(ChromeDriverManager().install())

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.implicitly_wait(10)
driver.get('https://jqueryui.com/droppable/')

# src = driver.find_element(By.ID, 'draggable')
# target = driver.find_element(By.ID, 'draggable')

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))

src = driver.find_element(By.XPATH, "//div[@id='draggable']")
target = driver.find_element(By.XPATH, "//div[@id='droppable']")

act_Chain = ActionChains(driver)
act_Chain.drag_and_drop(src, target).perform()
