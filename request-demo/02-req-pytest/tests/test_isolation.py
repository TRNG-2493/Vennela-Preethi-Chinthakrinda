import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

created_post_id=None

def test_create_post():
    global created_post_id
    
    response = requests.post(f"{BASE_URL}/posts",
                             json={"title":"Testing POST",
                                  "body":"Body for POST",
                                  "userId":1},
                             timeout=5
                             )
    assert response.status_code==201
    
    created_post_id=response.json()["id"]
    
def test_get_post():
    response=requests.get(f"{BASE_URL}/posts/{created_post_id}")
    assert response.status_code==200

# test 2 is dependent on test 1 and it is not isolation
# use fixtures or get the data before tests
