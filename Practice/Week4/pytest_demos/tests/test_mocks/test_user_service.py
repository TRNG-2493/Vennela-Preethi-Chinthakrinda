from mocks.user_service import welcome

from unittest.mock import Mock

def test_welcome():
    mock_get_user = Mock(return_value="Preethi")
    result = welcome(mock_get_user)
    assert result == "Hello Preethi"
    