import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

