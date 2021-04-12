from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html")



automationTool=driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Automation Tools')]")

action = ActionChains(driver)
action.move_to_element(automationTool).pause(3).click(driver.find_element(By.XPATH,"//a[text()='Appium']")).perform()


