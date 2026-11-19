import pytest
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    expect(inventory_page.title).to_have_text("Products")

@pytest.mark.parametrize(
    "user,pwd" ,[
        ("wrong_user", "secret_sauce"),
        ("standard_user","wrong"),
        ("","")
    ])    
def test_invalid_login(login_page,user,pwd):
    login_page.login(user,pwd)
    expect(login_page.error_message).to_be_visible()
    
    