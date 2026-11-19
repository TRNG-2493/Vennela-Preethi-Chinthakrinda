from playwright.sync_api import expect

def test_add_to_cart(logged_in_page):
    logged_in_page.click("[data-test = 'add-to-cart-sauce-labs-backpack']")
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")
    