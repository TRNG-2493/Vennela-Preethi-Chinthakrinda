import pytest
from playwright.sync_api import sync_playwright, Page, expect

def test_two_tabs(context):
    page1=context.new_page()
    page2=context.new_page()
    
    page1.goto("/")
    page2.goto("/")
    
    assert len(context.pages)==2
    
def test_print_browser(page,browser_name):
    print(f"Running on {browser_name}")
    
    