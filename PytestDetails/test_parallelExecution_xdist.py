import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.google.com/")
    print(driver.title)
    assert driver.title == "Google"
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.facebook.com/login.php")
    print(driver.title)
    assert driver.title == "Log in to Facebook"
    driver.quit()


def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.instagram.com/accounts/login/")
    print(driver.title)
    assert driver.title == "Login.Instagram"
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.gmail.com")
    print(driver.title)
    assert driver.title == "Gmail"
    driver.quit()


def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    print(driver.title)
    assert driver.title == "Rediffmail"
    driver.quit()
