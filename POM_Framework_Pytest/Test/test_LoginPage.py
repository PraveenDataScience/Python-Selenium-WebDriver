import pytest

from POM_Framework_Pytest.Config.config import TestData
from POM_Framework_Pytest.Pages.LoginPage import LoginPage
from POM_Framework_Pytest.Test.test_base import BaseTest


class test_login(BaseTest):

    def test_verify_homeLink(self):
        self.LoginPage=LoginPage(self.driver)
        flag=self.LoginPage.is_homeLink_exist()
        assert flag

    def test_loginPage_title(self):
        self.LoginPage = LoginPage(self.driver)
        title=self.LoginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title==TestData.LOGIN_PAGE_TITLE

    def test_login_ops(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_loginPage(TestData.USERNAME,TestData.PASSWORD)
