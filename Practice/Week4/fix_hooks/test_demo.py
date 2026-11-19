from playwright.sync_api import sync_playwright, expect, Page
def test_google_search():
    # Arrange, Act, Assert
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        
        context= browser.new_context()
        page=context.new_page();
        
        page.goto("https://www.google.com")
        
        expect(page).to_have_title("Google")
        
        page.close()

# fixture - work as setup code and cleanup code
def test_google_search_again(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")
    
    