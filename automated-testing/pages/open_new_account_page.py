from selenium.webdriver.common.by import By
from pages.account_services import AccountServices

class OpenNewAccount(AccountServices):
    
    def open_new_account(self, account_type, account_id):
        ACCOUNT_TYPE = (By.ID, "type")
        ACCOUNT_ID = (By.ID, "fromAccountId")
        OPEN_ACCOUNT_BUTTON = (By.XPATH, "//input[contains(@value,'Open New Account')]")

        self.select(ACCOUNT_TYPE, account_type)
        self.select(ACCOUNT_ID, account_id)
        self.click(OPEN_ACCOUNT_BUTTON)

        self.wait_for_page("Account Opened!")
