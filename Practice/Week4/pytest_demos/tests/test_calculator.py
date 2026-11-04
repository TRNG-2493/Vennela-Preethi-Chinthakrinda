import pytest
from calculator import add, multiply

@pytest.mark.smoke
def test_add():
    assert add(2, 3) == 5
    
# in-built assert
# testing framework it needs some configuration
# to run the test cases, we need to use pytest command in terminal
class TestMultiply:
    def test_multiply(self):
        assert multiply(2, 3) == 6

    def test_multiply_negative(self):
        assert multiply(-2, 3) == -6, f"Expected -6 but got {multiply(-2, 3)}"  
        
# how to execute with custom markers

# python -m <name of marker>