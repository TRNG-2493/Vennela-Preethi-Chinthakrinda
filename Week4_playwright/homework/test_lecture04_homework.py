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
    pass


def test_02_two_interests(store: Page):
    # TODO: tick "Newsletter" and "SMS updates"
    # TODO: #interests-summary says "Selected: Newsletter, SMS updates"
    pass


def test_03_select_all_then_untick_one(store: Page):
    # TODO: tick "Select all", then untick "SMS updates"
    # TODO: "Select all" is no longer checked
    # TODO: #interests-summary lists the two remaining interests
    pass


# ================= PART 2: Dropdowns =================

def test_04_country_by_label(store: Page):
    # TODO: choose "United States" BY LABEL
    # TODO: the dropdown's value is "us"
    # TODO: #country-summary says "Country: United States"
    pass


def test_05_sizes(store: Page):
    # TODO: in Sizes, choose M, L and XL; check all three are selected
    # TODO: then choose only XS; check that ONLY XS is selected now
    pass


def test_06_custom_dropdown(store: Page):
    # TODO: choose "Green" in the Colour dropdown
    # TODO: the button says "Colour: Green"
    # TODO: the colour list is hidden again
    pass


# ================= PART 3: Keyboard =================

def test_07_two_lines_of_notes(store: Page):
    # TODO: in Notes, type "Line 1", press Enter, type "Line 2"
    # TODO: the value is "Line 1\nLine 2"
    pass


def test_08_tab_between_fields(store: Page):
    # TODO: fill First name with "Ben", press Tab
    # TODO: Last name is focused
    # TODO: type "Carter" with the keyboard (don't use fill); check the value
    pass


def test_09_save_shortcut(store: Page):
    # TODO: press Ctrl+S (Cmd+S on macOS) - it must work on both!
    # TODO: #shortcut-result says "Saved with keyboard shortcut"
    pass


# ================= PART 4: Mouse =================

def test_10_hover_and_log_out(store: Page):
    # TODO: open the Account menu and click "Log out"
    # TODO: the URL contains "#logout"
    pass


def test_11_double_and_right_click(store: Page):
    # TODO: double-click "Double-click me"; it says "Edit mode"
    # TODO: right-click "Right-click here"; the menu has 2 items
    pass


def test_12_drag_and_drop(store: Page):
    # TODO: drag "Drag me" into the drop zone
    # TODO: #drop-result says "Dropped!"
    pass


# ================= PART 5: Auto-suggestions =================

def test_13_detroit_with_keyboard(store: Page):
    # TODO: type "de" in City
    # TODO: the suggestions are exactly ["Denver", "Detroit"]
    # TODO: choose Detroit using ONLY the keyboard
    # TODO: #city-summary says "City: Detroit"
    pass


def test_14_san_jose_with_mouse(store: Page):
    # TODO: type "san" in City; wait for 3 suggestions
    # TODO: click "San Jose"
    # TODO: City's value is "San Jose" AND the suggestion list is empty
    pass