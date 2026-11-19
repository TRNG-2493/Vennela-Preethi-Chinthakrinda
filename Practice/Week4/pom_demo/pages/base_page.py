from playwright.sync_api import Page
class BasePage:
    URL = "https://www.saucedemo.com"
    
    def __init__(self,page:Page):
        self.page=page
        
    def get_title(self)->str:
        return self.page.title()
    
    