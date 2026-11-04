from unittest.mock import Mock, patch
import requests
from mocks.weather_service import get_weather, display_weather


def test_display_weather():
    # arrange: mock the real api call - replace the original for time being
    requests.get = Mock()
    
    #when we call requets we get a response from response we get json from json we need temp value
    requests.get.return_value.json.return_value = {"temperature": 30}
    
    # act - execute the application function
    result = display_weather()
    # assert - verify the expected outcome
    assert result == "Temperature : 30"
    
    # how many times the mock was called and with what arguments
    requests.get.assert_called()
    requests.get.assert_called_once_with("https://api.example-weather.test/v1/current")
    
    
    # patch method - close automatically after the test is done
    
def test_display_weather_patch():
    with requests.patch("requests.get") as mock_api:
        mock_api.return_value.json.return_value = {"temperature": 35}
        result = display_weather()
        assert result == "Temperature : 35"
        mock_api.assert_called_once()
            
@patch("requests.get")
def test_display_weather_patch(mock_api):
    mock_api.return_value.json.return_value = {"temperature": 35}
    result = display_weather()
    assert result == "Temperature : 35"
    mock_api.assert_called_once()
        
@patch("requests.get")
def test_display_weather_sideeffect(mock_api):
    mock_api.side_effect = requests.exceptions.Timeout
    try:
        get_weather()
    except requests.exceptions.Timeout:
        print("API time out")

# is pytest having a mocker of its own - yes -pytest-mock is a wrapper
# we have a fixture - mockker fixture

def test_display_weather_mocker(mocker):
    mock_api = mocker.patch("requests.get")
    mock_api.return_value.json.return_value = {"temperature": 40}
    result = display_weather()
    assert result == "Temperature : 40"
       