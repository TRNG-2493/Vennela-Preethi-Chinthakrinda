import pytest
import requests

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def posts_data():
    return {
        "title":"Testing POST",
        "body":"Body for POST",
        "userId":1
    }
    
def test_get_post(api_url):
    response=requests.get(f"{api_url}/posts/1")
    
    assert response.status_code==200
    
def test_create_post(posts_data):
    payload=posts_data
    pass
