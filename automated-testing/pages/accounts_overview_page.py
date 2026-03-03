from selenium.webdriver.common.by import By
from .account_services import AccountServices

class AccountsOverview(AccountServices):

    def get_all_accounts_ids(self):
        locator = (By.XPATH, "//tr[td/a]/td/a")
        return self.get_text_of_all_elements(locator)

    def get_balance(self, account_id):
        locator = (By.XPATH, f"//a[text()='{account_id}']/parent::td/following-sibling::td[1]")
        return self.get_text(locator)
    
    def get_available_amount(self, account_id):
        locator = (By.XPATH, f"//a[text()='{account_id}']/parent::td/following-sibling::td[2]")
        return self.get_text(locator)
    
    