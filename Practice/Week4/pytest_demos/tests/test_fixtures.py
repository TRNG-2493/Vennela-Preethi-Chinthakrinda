import pytest
from cart import Cart

#@pytest.fixture
#def cart():
 #   return Cart()

def test_cart_initially_empty():
    cart = Cart()
    assert len(cart.items) == 0

def test_add_item():
    cart = Cart()
    cart.add_item("apple")
    assert "apple" in cart.items
    
    #with fixture each test gets a new cart
    
def test_currecy_from_config(app_config):
    assert app_config["currency"] == "USD"
    assert app_config["tax_rate"] == 0.1