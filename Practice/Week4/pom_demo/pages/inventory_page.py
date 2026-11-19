from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        
        # define locators
        self.title=page.locator(".title")
        self.items=page.locator(".inventory_items")
        self.cart_badge=page.locator(".shopping_cart_badge")
        self.cart_link=page.locator(".shopping_cart_link")
        self.sort_dropdown=page.locator("[data-test='product-sort-container']")
    
    # Actions
    
    def add_to_cart(self,Product_name:str):
        pass
    
    def go_to_cart(self):
        self.cart_link.click()
        
    def sort_by(self, option:str):
        pass
         