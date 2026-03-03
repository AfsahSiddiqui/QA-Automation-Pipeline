from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def select(self, locator, text_to_select):
        def option_present_in_dropdown(driver):
            dropdown = driver.find_element(*locator)
            select = Select(dropdown)
            return any(opt.text.strip() == text_to_select for opt in select.options)
        
        self.wait.until(option_present_in_dropdown)
        dropdown = self.wait.until(EC.visibility_of_element_located(locator))
        return Select(dropdown).select_by_visible_text(text_to_select)
    
    def get_text_of_all_elements(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return [el.text for el in elements]
    
    def wait_for_page(self, text):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,f"//h1[contains(text(),'{text}')]")))