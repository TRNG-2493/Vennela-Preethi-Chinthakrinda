from unittest.mock import Mock, patch

import pytest
import requests
import user_client
import responses

@responses.activate #tells we are using mocking
def test_get_username_returns_name():
    responses.add(
        responses.GET, "https://api.example.com/users/1",
        json={"id":1,"name":"John"},status=200
    )
    
    assert user_client.get_user(1)=="John"
    assert len(responses.calls)==1 
    #check the url
    assert responses.calls[0].request.url == "https://api.example.com/users/1"
    
def test_with_unit_test_mock():
    fake=Mock(status_code=200)
    fake.json.return_value={"name":"Doe"}
    with patch("user_client.requests.get",return_value=fake) as mocked:
        assert user_client.get_user(1)=="Doe"
    mocked.assert_called_once_with("https://api.example.com/users/1",timeout=5)
    