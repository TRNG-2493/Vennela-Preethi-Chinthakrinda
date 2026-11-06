from pathlib import Path
import pytest

from playwright.sync_api import Page, expect

PRACTICE_PAGE=Path(__file__).parent/"locators_practice.html"

# we cannot pass the file in ini file so we create a fixture
# go to page is 1st step
# locate the element is 2nd step
@pytest.fixture
def store(page:Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page
# exact 1 match to run the playwri with locators

# pass the fixture
def test_css_selectors(store:Page):
    #locator is a method
    expect(store.locator("h1")).to_have_text("Practice Store") # locates by tag
    email = store.locator("#email") #id locator, id locators start with #
    email.fill("vennela@example.com")
    expect(email).to_be_visible()
    product = store.locator(".product")
    expect(product).to_have_count(4)
    #locate password by using attribute locator
    password=store.locator("input[type='password']")
    

def test_xpath_selectors(store:Page):
    heading=store.locator("//h1") #directly jumps to element - relative path
    # /html/body/header/h1 - absolute path
    expect(heading).to_have_text("Practice Store")
    
    #using xpath locate email
    email=store.locator("//input[@placeholder='you@example.com']")
     
    #from header locate 2 elements
    #from login section find 2 elements
    #from form find 2 
    #from product find the price and in stock of some items 
    # in recent order find pending and cancelled
    # use both css and xpath
    