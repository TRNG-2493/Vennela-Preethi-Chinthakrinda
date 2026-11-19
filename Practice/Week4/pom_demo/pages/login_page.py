from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        # locators: define once use every where -are nouns
        self.username_input=page.locator("#user-name")
        self.password_input=page.locator("#password")
        self.login_button=page.locator("#login-button")
        self.error_message=page.locator("[data-test='error']")
        
# the benefit is if user changes the ids above, we just need to chnage here - (1 time)

# Actions
    def open(self):
        self.page.goto(self.URL)
        
    def login(self,username:str, password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
        

 