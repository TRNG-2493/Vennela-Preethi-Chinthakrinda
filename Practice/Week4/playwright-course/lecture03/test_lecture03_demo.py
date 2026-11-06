import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

PRACTICE_PAGE = Path(__file__).parent / "actions_practice.html"


@pytest.fixture
def store(page: Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page


def test_fill_and_click_successful_login(store:Page):
    store.get_by_label("Username").press_sequentially("student")
    store.get_by_label("Password").fill("secret123")
    store.get_by_role("button", name = "Log in").click()
    expect(store.locator("#login-message")).to_have_text("Welcome, student!")
    
def test_failed_login(store:Page):
    store.get_by_label("Username").press_sequentially("student")
    store.get_by_label("Password").fill("prac12")
    store.get_by_role("button", name = "Log in").click()
    expect(store.locator("#login-message")).to_have_text("Invalid username or password")
        
def test_clear_username(store:Page):
    #locate username
    #fill by value = student
    # clear the text box
    # check the username textbox to be empty
    username = store.get_by_label("Username")
    username.fill("student")
    username.clear()
    expect(username).to_have_value("")
    
'''
def test_click_multiple_times(store:Page):
    # locate add button
    # click it 3 times
    # check cart to have items = 3
    add_button = store.get_by_role("button", name="Add to cart")
    for _ in range(3):
        add_button.click()
    expect(store.locator(".cart-count")).to_have_text("3")def test_click_multiple_times(store:Page):
    # locate add button
    # click it 3 times
    # check cart to have items = 3
    add_button = store.get_by_role("button", name="Add to cart")
    for _ in range(3):
        add_button.click()
    expect(store.locator(".cart-count")).to_have_text("3")'''
    

#locate if terms checkbox is enabled or not
def test_unchecked_terms_button_disabled(store:Page):
    check_box=store.get_by_role("checkbox")
    check_box.uncheck()
    continue_button = store.get_by_text("Continue")
    expect(continue_button).to_be_disabled()

def test_checked_terms_button_enabled(store:Page):
    check_box=store.get_by_role("checkbox")
    check_box.check()
    continue_button = store.get_by_text("Continue")
    expect(continue_button).to_be_enabled()
    
