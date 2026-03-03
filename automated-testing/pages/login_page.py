from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.accounts_overview_page import AccountsOverview

class LoginPage(BasePage):

    USERNAME = (By.XPATH, "//input[contains(@name,'username')]")
    PASSWORD = (By.XPATH, "//input[contains(@name,'password')]")
    LOGIN_BUTTON = (By.XPATH, "//input[contains(@value,'Log In')]")
     
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

        self.wait_for_page("Accounts Overview")

        return AccountsOverview(self.driver)