import pytest
from calculator import divide

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(6, 0)
        
def test_divide_negative():
    assert divide(-6, 3) == -2 
    
def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(10, 0)
        
def test_divide_execinfo():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "divide by zero" in str(excinfo.value)
    assert excinfo.type == ValueError