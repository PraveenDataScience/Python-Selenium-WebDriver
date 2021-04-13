from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("===========SETUP===============")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")

    yield
    print("===========SETUP===============")
    driver.quit()

'''
def test_google_title(init_driver):
    assert driver.title == "Google"


def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.com/"
'''


@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"


@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.co/"