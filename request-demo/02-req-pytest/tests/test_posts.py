# we are testing the post endpoint

import requests
import pytest 

BASE_URL= "https://jsonplaceholder.typicode.com/"

#response=requests.get(f"{BASE_URL}/posts/1", timeout=5);

def test_get_post_return_200():
    # arrange
    url=f"{BASE_URL}/posts/1"
    # act
    resp=requests.get(url,timeout=5)
    # assert
    assert resp.status_code == 200

@pytest.mark.smoke    
def test_post_has_expected_id():
    url=f"{BASE_URL}/posts/1"
    resp=requests.get(url,timeout=5)
    body=resp.json()
    assert body["id"]==1,f"Unexpected body: {body}"
