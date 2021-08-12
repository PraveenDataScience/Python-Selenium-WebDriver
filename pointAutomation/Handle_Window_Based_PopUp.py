import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(10)


driver.get("http://www.facebook.com")

#get the window handle after the window has opened:
window_before=driver.window_handles[0]
print(window_before)
window_before_title=driver.title
print(window_before_title)

#Open a new window:
driver.execute_script("window.open('http://www.twitter.com','new window')")

#get the window handle after a new window has opened:
window_after=driver.window_handles[1]

#Switch to new Child window:
driver.switch_to.window(window_after)
time.sleep(10)

window_after_title=driver.title
print(window_after_title)

#Compare and verify that main window & child window title did not match:
if window_before_title!=window_after_title:
    print("Context switched to Twitter,so the title did not match")
else:
    print("Control did not switch to new window")


#Now switch back to Original window:
driver.switch_to.window(window_before)

#verify that title should match now:
if window_before_title==driver.title:
    print("Context returned to parent window. Title now matched")

print(driver.title)

