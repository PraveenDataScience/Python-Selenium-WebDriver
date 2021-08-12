import webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#webdriver_manager.chrome(ChromeDriverManager().install())
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://demo.automationtesting.in/Frames.html")

frame_element=driver.find_element(By.XPATH,"//iframe[@id='singleframe']")
driver.switch_to.frame(frame_element)
#frame_element2=driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']")
#driver.switch_to.frame(frame_element2)
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Welcome!!")
