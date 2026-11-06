import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

PRACTICE_PAGE = Path(__file__).parent / "forms_practice.html"


@pytest.fixture
def store(page: Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page

# check radio buttons have total count of 4
def test_check_count_of_radio_buttons(store:Page):
    expect(store.get_by_role("radio")).to_have_count(4)


# check the express radio button, 3 expect buttons make sure express is checked, standard is uncheck, text Shipping: Express
def test_check_express_radio_button(store:Page):
    store.get_by_label("Express").check()
    expect(store.get_by_label("Express")).to_be_checked()
    expect(store.get_by_label("Standard")).not_to_be_checked()
    expect(store.locator("#shipping-summary")).to_have_text("Shipping: Express")

#check and confirm store-pickup is disabled
def test_store_pickup_button_is_disabled(store:Page):
    expect(store.get_by_label("pickup")).to_be_disabled()


# check on newsletter expect that newsletter is checked
# and text is visible 2 checks 1 action
def test_newsletter_check(store:Page):
    store.get_by_text("newsletter").check()
    expect(store.get_by_text("newsletter")).to_be_checked
    expect(store.locator("#interests-summary")).to_have_text("Selected: Newsletter")
    
# same two checks
def test_newsletter_and_special_offer_check(store:Page):
    store.get_by_text("newsletter").check()
    store.get_by_text("offers").check()
    expect(store.get_by_text("newsletter")).to_be_checked
    expect(store.get_by_text("offers")).to_be_checked
    expect(store.locator("#interests-summary")).to_have_text("Selected: Newsletter, Special offers")

# select all checked check it

def test_select_all_check(store:Page):
    store.get_by_label("Select All").check()
    for box in store.locator(".interest").all():
        expect(box).to_be_checked()

def test_select_by_label(store:Page):
    # retuen element whose label is country
    store.get_by_label("Country").select_option(label="Canada")
    expect(store.locator("#country-summary")).to_have_text("Country: Canada")
    # return by value
    store.get_by_label("Country").select_option("uk")
    expect(store.locator("#country-summary")).to_have_text("Country: United Kingdom")

    #return by index
    store.get_by_label("Country").select_option(index=2)
    expect(store.locator("#country-summary")).to_have_text("Country: India")

    
def test_multiple_select(store:Page):
    store.get_by_label("Sizes").select_option(["s","m","l"])
    
    