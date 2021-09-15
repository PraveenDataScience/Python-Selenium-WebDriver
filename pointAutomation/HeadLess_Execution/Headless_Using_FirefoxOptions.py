from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

options=webdriver.FirefoxOptions()
options.headless=True

driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
driver.get("https://www.reddit.com/")

title=driver.title
print(title)