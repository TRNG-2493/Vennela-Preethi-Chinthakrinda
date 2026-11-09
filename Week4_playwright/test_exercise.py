from pathlib import Path
import pytest

from playwright.sync_api import Page, expect

PRACTICE_PAGE=Path(__file__).parent/"locators_practice.html"

@pytest.fixture
def store(page:Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page

# PART - A

def test_css_selectors(store:Page):
    # 1. The main page heading
    loc = store.locator("h1")
    expect(loc).to_have_text("Practice Store")
    
    # 2. The email input, using its id
    loc = store.locator("#email")
    expect(loc).to_have_attribute("type","email")
    
    # 3. The password input, using its type attribute
    loc = store.locator("[type='password']")
    expect(loc).to_have_attribute("placeholder", "Enter password")
    
    # 4. The "Remember me" checkbox, using its id
    loc = store.locator("#remember")
    expect(loc).not_to_be_checked()
    
    # 5. The Sign in button, using its type attribute
    loc = store.locator("[type='submit']")
    expect(loc).to_have_text("Sign in")
    
    # 6. The logo image, using its alt attribute
    loc = store.locator("[alt = 'Practice Store logo']")
    expect(loc).to_have_attribute("src", "logo.png")
    
    # 7. All links inside the navigation bar
    loc = store.locator("nav a")
    expect(loc).to_have_text(["Home", "Products", "Contact us"])
    
    # 8. The "Contact us" link, using its href
    loc = store.locator("[href = '#contact']")
    expect(loc).to_have_text("Contact us")
    
    # 9. The 🚚 icon, using a partial match on its title (contains "shipping")
    loc = store.locator("[title*='shipping']")
    expect(loc).to_have_attribute("title", "Free shipping on orders over $50")
    
    # 10. The Checkout button, using its data-testid
    loc = store.locator("[data-testid = 'checkout-button']")
    expect(loc).to_have_text("Checkout")
    
    # 11. All product items
    loc = store.locator(".product-list .product")
    expect(loc).to_have_count(4)
    
    # 12. All product prices
    loc = store.locator(".product-list .product .price")
    expect(loc).to_have_text(["$29.99", "$9.99", "$15.99", "$49.99"])
    
    # 13. The disabled "Add to cart" button
    loc = store.locator("[disabled]")
    expect(loc).to_be_disabled
    
    # 14. All "Add to cart" buttons that are not disabled
    loc = store.locator("button:not(:disabled)").filter(has_text="Add to cart")
    expect(loc).to_have_count(3)
    
    # 15. The name of the first product
    loc = store.locator(".product").first.locator("h3")
    expect(loc).to_have_text("Backpack")
    
    # 16. The price of the third product
    loc = store.locator(".product").nth(2).locator(".price")
    expect(loc).to_have_text("$15.99")
    
    # 17. The stock status of the last product
    loc = store.locator(".product").nth(3).locator(".stock")
    expect(loc).to_have_text("In stock")
    
    # 18. All h2 headings that are direct children of a section
    loc = store.locator("section > h2")
    expect(loc).to_have_text(["Sign in", "Products", "Recent orders"])
    
    # 19. All rows in the orders table body (not the header row)
    loc = store.locator("table tbody tr")
    expect(loc).to_have_count(4)
    
    # 20. The status cell of the second order row
    loc = store.locator("table tbody tr:nth-child(2) td:nth-child(3)")
    expect(loc).to_have_text("Pending")


# PART - B
def test_xpath_selectors(store:Page):
    
    #using xpath locate email
    #email=store.locator("//input[@placeholder='you@example.com']")
    
    # 1. The third link in the nav, by position
    loc = store.locator("//nav/a[3]")
    expect(loc).to_have_text("Contact us")
    
    # 2. The password input, using its id attribute
    loc = store.locator("//form/input[@id='password']")
    expect(loc).to_have_attribute("type", "password")
    
    # 3. The email input, using its placeholder
    loc = store.locator("//form/input[@placeholder='you@example.com']")
    expect(loc).to_be_empty()
    
    # 4. The "Home" link, using its exact text
    loc = store.locator("//nav/a[text()='Home']")
    expect(loc).to_have_attribute("href", "#home")
    
    # 5. The "Forgot password?" link, using partial text ("Forgot")	
    loc = store.locator("//a[contains(text(), 'Forgot')]")
    expect(loc).to_have_text("Forgot password?")

	# 6. The Sign in button (not the heading), using its text	
    loc = store.locator("//button[(text()='Sign in')]")
    expect(loc).to_have_attribute("type", "submit")
	
    # 7. The checkbox inside the label that contains "Remember me"	
    loc = store.locator("//label[contains(., 'Remember me')]//input[@type='checkbox']")
    expect(loc).to_have_id("remember")

    # 8. The Checkout button, using its text
    loc = store.locator("//button[text()='Checkout']")
    expect(loc).to_have_attribute("data-testid", "checkout-button")
    
    # 9. All product li elements, using the class attribute
    loc = store.locator("//li[@class='product']")
    expect(loc).to_have_count(4)
    
    # 10. The product heading with the text "Jacket"
    loc = store.locator("//h3[text()='Jacket']")
    expect(loc).to_be_visible()
    
    # 11. The price of "Bike Light", starting from its heading (use a sibling axis)
    loc = store.locator("//h3[text()='Bike Light']/following-sibling::p[@class='price']")
    expect(loc).to_have_text("$9.99")
    
    # 12. The name of the product that is "Out of stock" (go up to the parent, then down)
    loc = store.locator("//*[text()='Out of stock']/../h3")
    expect(loc).to_have_text("Bike Light")
    
    # 13. The "Add to cart" button of the "T-Shirt" product
    loc = store.locator("//h3[text()='T-Shirt']/following-sibling::button[text()='Add to cart']")
    expect(loc).to_be_enabled()
    
    # 14. All buttons that have the disabled attribute
    loc = store.locator("//button[@disabled]")
    expect(loc).to_have_count(1)
    
    # 15. The heading of the second product, using ( … )[n] indexing
    loc = store.locator("(//li[@class='product']//h3)[2]")
    expect(loc).to_have_text("Bike Light")
    
    # 16. The last price on the page, using last()
    loc = store.locator("(//p[@class='price'])[last()]")
    expect(loc).to_have_text("$49.99")
    
    # 17. All stock paragraphs whose text is exactly "In stock"
    loc = store.locator("//p[@class='stock' and text()= 'In stock']")
    expect(loc).to_have_count(3)
    
    # 18. The status of the order placed by "Chen Wei"
    loc = store.locator("//tr[td[text()='Chen Wei']]/td[3]")
    expect(loc).to_have_text("Shipped")
    
    # 19. The order number of the "Pending" order (use a preceding-sibling axis)
    loc = store.locator("//td[text()='Pending']/preceding-sibling::td[2]")
    expect(loc).to_have_text("1002")
    
    # 20. The total of the "Cancelled" order
    loc = store.locator("//tr[td[text()='Cancelled']]/td[4]")
    expect(loc).to_have_text("$15.99")
    