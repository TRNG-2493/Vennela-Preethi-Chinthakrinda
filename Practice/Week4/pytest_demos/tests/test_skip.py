import pytest
from calculator import divide

#
@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_divide():
    assert divide(6, 3) == 2    

# xfail is used to mark a test that is expected to fail. It can be useful when you have a known issue or bug that you want to track, but you don't want it to cause the entire test suite to fail.
@pytest.mark.xfail(reason="This test is expected to fail for demonstration purposes")
def test_divide_by_zero():
    assert divide(6, 0) == 0
    
#skipping inside a test


#custom markers
#@pytest.mark.smoke