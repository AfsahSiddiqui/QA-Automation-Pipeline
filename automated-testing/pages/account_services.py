from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountServices(BasePage):
    
    def select_service(self, service_name):
        service_title = service_name.title()
        locator = (By.XPATH, f"//a[contains(text(),'{service_title}')]")
        self.click(locator)
        self.wait_for_page(service_title)

        if service_title == "Open New Account":
            from pages.open_new_account_page import OpenNewAccount
            return OpenNewAccount(self.driver)
        
        if service_title == "Accounts Overview":
            from pages.accounts_overview_page import AccountsOverview
            return AccountsOverview(self.driver)
    