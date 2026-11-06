# 1. Which locators did codegen choose for the username, password and Log in button?
# The codegen used textbox for username, password, and button for Log in button

# 2. Which generated lines are unnecessary?
# The unnecessary lines are lines having .click(). Because .fill() automatically focuses the input before entering text.

# 3. What important thing is missing from the recorded test?
# expect assertions

# 4. What would you change before using this as a real test?
# use expect and use wait where ever necessary and remove the unnecessary lines


import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("file:///C:/Users/chvpr/Documents/Revature/Week4_playwright/homework/actions_practice.html")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("secret123")
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("searchbox", name="Search products").click()
    page.get_by_role("searchbox", name="Search products").fill("jacket")
    page.get_by_role("searchbox", name="Search products").press("Enter")


