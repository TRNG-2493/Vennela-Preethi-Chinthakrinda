import re
from pathlib import Path
import time

import pytest
from playwright.sync_api import Page, expect

PRACTICE_PAGE = Path(__file__).parent / "actions_practice.html"


@pytest.fixture
def store(page: Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page


# ================= PART 1: Actions and assertions =================

def test_01_successful_login(store: Page):
    # TODO: log in with student / secret123
    # TODO: the message (#login-message) says "Welcome, student!"
    # TODO: the message has the class "success"
    # TODO: the URL contains "#dashboard"
    store.get_by_label("Username").press_sequentially("student")
    store.get_by_label("Password").fill("secret123")
    store.get_by_role("button", name = "Log in").click()
    expect(store.locator("#login-message")).to_have_text("Welcome, student!")
    expect(store.locator("#login-message")).to_have_class("success")
    expect(store).to_have_url(re.compile(r".*#dashboard"))

def test_02_failed_login(store: Page):
    # TODO: log in with student / a wrong password
    # TODO: the message says "Invalid username or password"
    # TODO: the message has the class "error"
    # TODO: the URL does NOT contain "#dashboard"
    store.get_by_label("Username").fill("student")
    store.get_by_label("Password").fill("pass00")
    store.get_by_role("button", name = "Log in").click()
    expect(store.locator("#login-message")).to_have_text("Invalid username or password")
    expect(store.locator("#login-message")).to_have_class("error")
    expect(store).not_to_have_url(re.compile(r".*#dashboard"))

def test_03_empty_login(store: Page):
    # TODO: click "Log in" without filling anything
    # TODO: the error message appears
    store.get_by_role("button", name = "Log in").click()
    expect(store.locator("#login-message")).to_have_text("Invalid username or password")

def test_04_search_with_enter(store: Page):
    # TODO: search for "bike light" and press Enter
    # TODO: #search-result says "Results for: bike light"
    search = store.get_by_placeholder("Search products")
    search.fill("bike light")
    search.press("Enter")
    expect(store.locator("#search-result")).to_have_text("Results for: bike light")


def test_05_add_five_items(store: Page):
    # TODO: click "Add item" 5 times (use a loop)
    # TODO: #cart-count says "Items: 5"
    add_button = store.get_by_role("button", name="Add item")
    for _ in range(5):
        add_button.click()
    expect(store.locator("#cart-count")).to_have_text("Items: 5")


def test_06_terms_toggle(store: Page):
    # TODO: "Continue" is disabled
    # TODO: tick "I agree to the terms" -> "Continue" is enabled
    # TODO: untick it -> "Continue" is disabled again
    continue_button=store.get_by_role("button", name="Continue")
    expect(continue_button).to_be_disabled()
    store.get_by_role("checkbox").check()
    expect(continue_button).to_be_enabled()
    store.get_by_role("checkbox").uncheck()
    expect(continue_button).to_be_disabled()

# ================= PART 2: Dynamic elements =================

def test_07_load_products(store: Page):
    # TODO: click "Load products"
    # TODO: "Loading..." is visible, then hidden
    # TODO: exactly 3 products are listed (#product-list li)
    # TODO: the last product is "Jacket"
    store.get_by_role("button", name =" Load products").click()
    expect(store.locator("#spinner")).to_have_text("Loading...")
    expect(store.locator("#spinner")).to_be_hidden()
    expect(store.locator("#product-list li").last).to_have_text("Jacket")


def test_08_process_order(store: Page):
    # TODO: click "Process order"
    # TODO: #order-status eventually says "Complete"
    store.get_by_role("button", name="Process order").click()
    expect(store.locator("#order-status")).to_have_text("Complete")


def test_09_slow_report(store: Page):
    # TODO: click "Generate report"
    # TODO: #report-result says "Report ready"
    # Hint: this takes 7 seconds. What does expect need?
    store.get_by_role("button", name="Generate report").click()
    #expect(store.locator("#report-result")).to_be_visible()
    expect(store.locator("#report-result")).to_have_text("Report ready", timeout = 9000)
    
    
# Answer as comments at the bottom of test_lecture03_homework.py:

# 1. How many actions are listed?
# 8 actions are listed

# 2. Click the Log in click action and open the After tab. What does the message say at that moment?
# Checking...

# 3. Click your to_have_text assertion. Roughly how long did it wait?
# 1.4 seconds



def test_flaky_login(page: Page):
    page.goto(PRACTICE_PAGE.as_uri())
    page.locator("#username").fill("student")
    page.locator("#password").fill("secret123")
    page.locator("#login-button").click()
    time.sleep(1)
    assert page.locator("#login-message").text_content() == "Welcome, student!"
    
# Explain in a comment what's wrong with it (there are at least 2 problems).
# time.sleep is hard-coded wait, time is wasted if page is loaded and it fails if the page takes 
# more time to load than that and assert is used - which is not recommended to use as
# assert will not wait until locators are found and there are no expect assertions

# Write a fixed version called test_fixed_flaky_login.
def test_fixed_flaky_login(store:Page):
    store.locator("#username").fill("student")
    store.locator("#password").fill("secret123")
    store.get_by_role("button", name = "Log in").click()
    expect(store.locator("#login-message")).to_have_text("Welcome, student!")
    