import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

PRACTICE_PAGE = Path(__file__).parent / "forms_practice.html"


@pytest.fixture
def store(page: Page) -> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page


def suggestions(page: Page):
    """The options inside the city suggestions list only."""
    return page.get_by_role("listbox", name="Suggestions").get_by_role("option")


# ================= PART 1: Radio buttons and checkboxes =================

def test_01_overnight_shipping(store: Page):
    # TODO: choose "Overnight"
    # TODO: Overnight is checked AND Standard is not checked
    # TODO: #shipping-summary says "Shipping: Overnight"
    loc = store.get_by_label("Overnight")
    loc.check()
    expect(loc).to_be_checked()
    expect(store.get_by_text("Standard")).not_to_be_checked()  
    expect(store.locator("#shipping-summary")).to_have_text("Shipping: Overnight")

def test_02_two_interests(store: Page):
    # TODO: tick "Newsletter" and "SMS updates"
    # TODO: #interests-summary says "Selected: Newsletter, SMS updates"
    loc1 = store.get_by_label("newsletter")
    loc2 = store.get_by_label("sms")
    loc1.check()
    loc2.check()
    expect(store.locator("#interests-summary")).to_have_text("Selected: Newsletter, SMS updates")


def test_03_select_all_then_untick_one(store: Page):
    # TODO: tick "Select all", then untick "SMS updates"
    # TODO: "Select all" is no longer checked
    # TODO: #interests-summary lists the two remaining interests
    loc1 = store.get_by_label("Select all")
    loc1.check()
    loc2 = store.get_by_label("sms")
    loc2.uncheck()
    expect(store.locator("#select-all")).not_to_be_checked()
    expect(store.locator("#interests-summary")).to_have_text("Selected: Newsletter, Special offers")
# ================= PART 2: Dropdowns =================

def test_04_country_by_label(store: Page):
    # TODO: choose "United States" BY LABEL
    # TODO: the dropdown's value is "us"
    # TODO: #country-summary says "Country: United States"
    loc = store.get_by_label("Country")
    loc.select_option(label="United States")
    expect(loc).to_have_value("us")
    expect(store.locator("#country-summary")).to_have_text("Country: United States")


def test_05_sizes(store: Page):
    # TODO: in Sizes, choose M, L and XL; check all three are selected
    # TODO: then choose only XS; check that ONLY XS is selected now
    loc = store.get_by_label("Sizes")
    loc.select_option(["M", "L", "XL"])
    expect(store.locator("#sizes-summary")).to_have_text("Sizes: M, L, XL")
    loc.select_option("XS")
    expect(store.locator("#sizes-summary")).to_have_text("Sizes: XS")


def test_06_custom_dropdown(store: Page):
    # TODO: choose "Green" in the Colour dropdown
    # TODO: the button says "Colour: Green"
    # TODO: the colour list is hidden again
    store.get_by_role("button", name="Choose a colour").click()
    loc = store.locator("#colour-list")
    expect(loc).to_be_visible()
    loc.get_by_role("option", name="Green").click()
    expect(loc).to_be_hidden()
    
# ================= PART 3: Keyboard =================

def test_07_two_lines_of_notes(store: Page):
    # TODO: in Notes, type "Line 1", press Enter, type "Line 2"
    # TODO: the value is "Line 1\nLine 2"
    loc=store.locator("#notes")
    loc.fill("Line 1\nLine2")
    expect(loc).to_have_value("Line 1\nLine2")


def test_08_tab_between_fields(store: Page):
    # TODO: fill First name with "Ben", press Tab
    # TODO: Last name is focused
    # TODO: type "Carter" with the keyboard (don't use fill); check the value
    loc1=store.locator("#first-name")
    loc2=store.locator("#last-name")
    loc1.fill("Ben")
    loc1.press("Tab")
    expect(loc2).to_be_focused
    loc2.press_sequentially("Carter")
    expect(loc1).to_have_value("Ben")
    expect(loc2).to_have_value("Carter")
    
def test_09_save_shortcut(store: Page):
    # TODO: press Ctrl+S (Cmd+S on macOS) - it must work on both!
    # TODO: #shortcut-result says "Saved with keyboard shortcut"
    store.keyboard.press("ControlOrMeta+S")
    expect(store.locator("#shortcut-result")).to_have_text("Saved with keyboard shortcut")
    
# ================= PART 4: Mouse =================

def test_10_hover_and_log_out(store: Page):
    # TODO: open the Account menu and click "Log out"
    # TODO: the URL contains "#logout"
    store.get_by_role("button", name ="Account").hover()
    store.get_by_text(" Log out", exact = True).click()
    expect(store).to_have_url(re.compile(r"#logout"))

def test_11_double_and_right_click(store: Page):
    # TODO: double-click "Double-click me"; it says "Edit mode"
    # TODO: right-click "Right-click here"; the menu has 2 items
    store.get_by_text("Double-click me", exact=True).dblclick()
    expect(store.get_by_text("Edit mode")).to_be_visible()
    store.get_by_text("Right-click here", exact=True).click(button="right")
    expect(store.get_by_role("menuitem")).to_have_count(2)


def test_12_drag_and_drop(store: Page):
    # TODO: drag "Drag me" into the drop zone
    # TODO: #drop-result says "Dropped!"
    loc1=store.get_by_text("Drag me", exact=True)
    loc2=store.get_by_text("Drop here", exact=True)
    loc1.drag_to(loc2)
    expect(store.locator("#drop-result")).to_have_text("Dropped!")

# ================= PART 5: Auto-suggestions =================

def test_13_detroit_with_keyboard(store: Page):
    # TODO: type "de" in City
    # TODO: the suggestions are exactly ["Denver", "Detroit"]
    # TODO: choose Detroit using ONLY the keyboard
    # TODO: #city-summary says "City: Detroit"
    city = store.get_by_label("City")
    suggestions = store.locator("#suggestions")
    city.fill("de")
    expect(suggestions.get_by_role("option")).to_have_text(
        ["Denver", "Detroit"])
    city.press("ArrowDown")
    city.press("ArrowDown")
    city.press("Enter")
    expect(store.locator("#city-summary")).to_have_text("City: Detroit")
    
    
def test_14_san_jose_with_mouse(store: Page):
    # TODO: type "san" in City; wait for 3 suggestions
    # TODO: click "San Jose"
    # TODO: City's value is "San Jose" AND the suggestion list is empty
    city = store.get_by_label("City")
    suggestions = store.locator("#suggestions")
    city.fill("san")
    options = suggestions.get_by_role("option")
    expect(options).to_have_count(3)
    options.filter(has_text="San Jose").click()
    expect(city).to_have_value("San Jose")
    expect(options).to_have_count(0)