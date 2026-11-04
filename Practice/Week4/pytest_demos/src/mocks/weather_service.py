# mock a resource
# requests is a module to send requests to endpoint
import requests

# resource
API_URL = "https://api.example-weather.test/v1/current"

# request
def get_weather():
    response = requests.get(API_URL)
    return response.json()

def display_weather():
    weather=get_weather()
    return f"Temperature : {weather['temperature']}"
# display weather is depend on get_weather and get weather is depend on api
# if server/api is down then it will fail
# to do unit test we need to mock

