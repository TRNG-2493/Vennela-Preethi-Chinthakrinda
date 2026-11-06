from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

PRACTICE_PAGE = Path(__file__).parent / "locators_practice.html"


@pytest.fixture
def store(page: Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page


# ================= PART 1: Built-in locators =================
# Rule: use ONLY get_by_role, get_by_label, get_by_placeholder,
#       get_by_text, get_by_alt_text, get_by_title or get_by_test_id.
#       No page.locator() in Part 1!

def test_01_products_link(store: Page):
    # TODO: the "Products" LINK in the navigation is visible
    pass


def test_02_recent_orders_heading(store: Page):
    # TODO: the "Recent orders" heading is visible
    pass


def test_03_password_by_label(store: Page):
    # TODO: find the Password field by its label; check it is empty
    # Hint: expect(...).to_be_empty()
    pass


def test_04_email_by_placeholder(store: Page):
    # TODO: find the Email field by its placeholder; check it is visible
    pass


def test_05_remember_me_checkbox(store: Page):
    # TODO: the "Remember me" checkbox is NOT checked
    # Hint: expect(...).not_to_be_checked()
    pass


def test_06_logo_by_alt_text(store: Page):
    # TODO: find the logo image by its alt text; check it is attached
    # Hint: expect(...).to_be_attached()
    pass


def test_07_shipping_icon_by_title(store: Page):
    # TODO: find the shipping icon by its title; check it is visible
    pass


def test_08_checkout_by_test_id(store: Page):
    # TODO: find the Checkout button by its test id; check it is visible
    pass


def test_09_copyright_text(store: Page):
    # TODO: the footer text "2026 Practice Store" is visible
    pass


def test_10_privacy_link(store: Page):
    # TODO: the "Privacy policy" link is visible
    pass


# ================= PART 2: Filtering and chaining =================
# You may use page.locator(".product") as a starting point here.

def test_a_tshirt_price(store: Page):
    # TODO: in the T-Shirt product card, the price is "$15.99"
    # Hint: filter(has_text=...) then find ".price" inside it
    pass


def test_b_in_stock_count(store: Page):
    # TODO: exactly 3 products are "In stock"
    # Hint: expect(...).to_have_count(3)
    pass


def test_c_order_status(store: Page):
    # TODO: in the orders table, Ben Carter's order status is "Pending"
    # Hint: find the row, then the cells inside it. Which nth() is Status?
    pass


def test_d_first_and_last(store: Page):
    # TODO: the LAST product name is "Jacket"
    # TODO: the FIRST product price is "$29.99"
    pass


def test_e_bike_light_disabled(store: Page):
    # TODO: the Bike Light's "Add to cart" button is disabled
    # Hint: expect(...).to_be_disabled()
    pass


# ================= PART 2 QUESTION =================
# Answer as a comment:
# What happens if you run
#     store.get_by_role("button", name="Add to cart").click()
# and how would you change it to click ONLY the Jacket's button?