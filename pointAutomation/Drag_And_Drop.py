from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get('https://jqueryui.com/droppable/')
driver.maximize_window()

frameElement=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frameElement)
src = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

act_chain = ActionChains(driver)
act_chain.drag_and_drop(src, target).perform()