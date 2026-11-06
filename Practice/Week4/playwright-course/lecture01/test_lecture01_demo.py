import re
from playwright.sync_api import Page, expect

def test_home_page_title(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_title("The Internet")

def test_homepage_shows_welcome_heading(page: Page):
    page.goto("/")
    heading = page.get_by_role("heading", name = "Welcome to the-internet")
    expect(heading).to_be_visible()

def test_open_login_page_directly(page: Page):
    page.goto("/login")
    heading = page.get_by_role("heading", name = "Login Page")
    expect(heading).to_be_visible
    
def test_open_login_page_by_clicking_link(page:Page):
    page.goto("/")
    page.get_by_role("link", name = "Form Authentication").click()
    expect(page.get_by_role("heading",name="Login Page")).to_be_visible()
    