from POM_Framework_Pytest.Config.config import TestData
from POM_Framework_Pytest.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    '''By_Locators : OR'''
    USER_NAME =(By.NAME,'userName')
    PASSWORD =(By.NAME,'password')
    SUBMIT_BTN=(By.XPATH,"input[name='submit']")

    HOME_LINK=(By.LINK_TEXT,"Home")

    '''Constructor of page class'''
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """PAGE ACTIONS"""
    '''this is used for login page title'''
    def get_loginPage_title(self,title):
        return self.get_title(title)

    '''this is used to check home link on login page'''
    def is_homeLink_exist(self):
        return self.is_visible(self.HOME_LINK)

    '''this is used to login the app: '''
    def do_loginPage(self,username,password):
        self.do_sen_keys(self.USER_NAME,username)
        self.do_sen_keys(self.PASSWORD,password)
        self.do_click(self.SUBMIT_BTN)


