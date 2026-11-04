import pytest

from calculator import is_even, add

@pytest.mark.parametrize('number', [2, 4, 6, 8, 10])
def test_iseven(number):
    
    '''assert iseven(4) == True
    assert iseven(5) == False   
    assert iseven(0) == True
    assert iseven(-2) == True
    assert iseven(-3) == False'''
    
    assert is_even(number)

@pytest.mark.parametrize('a,b,expected', [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (-2, -3, -5),
    (100, 200, 300)
])   
def test_add(a,b,expected):
    assert add(a,b) == expected