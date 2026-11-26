import requests
import pytest

BASE_URL= "https://jsonplaceholder.typicode.com/"

def test_user_has_required_fields():
    r=requests.get(f"{BASE_URL}/users/1",timeout=5)
    user=r.json();
    #assert r.status_code == 200
    for field in ("id","name","email","address"):
        assert field in user, f"missing{field}"
    
#take this url, pass a query parameter, userid = 1 and check the length of post is 10
# within the same method, also assert all post methods belong to user id 1

def test_posts_belong_to_user():
    r = requests.get(
        f"{BASE_URL}/posts",
        params={"userId": 1},
        timeout=5
    )
    post = r.json()
    assert len(post) == 10
    for p in post:
        assert p["userId"] == 1
        

    
    