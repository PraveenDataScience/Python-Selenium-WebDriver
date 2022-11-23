import pytest
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from POM_Framework_Pytest.Config.config import TestData


@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
    if request.params=='chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.params=='firefox':
        web_driver=webdriver.Firefox(TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver=web_driver
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()

    yield
    web_driver.quit()