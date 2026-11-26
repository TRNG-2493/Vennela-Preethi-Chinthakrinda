import pytest
import requests
import json

BASE_URL= "https://jsonplaceholder.typicode.com/"

@pytest.mark.parametrize("user_id",[1,2,3,5])
def test_get_user(user_id):
    resp=requests.get(f"{BASE_URL}/users/{user_id}")
    assert resp.status_code == 200
    data=resp.json()
    
    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data
    
@pytest.mark.parametrize("user_id",[101,102])    
def test_invalid_user(user_id):
    resp=requests.get(f"{BASE_URL}/users/{user_id}")
    data=resp.json()
    assert resp.status_code == 404
    assert data == {}, "Not valid user, json should be empty"

@pytest.mark.parametrize(
    "post_id, expected_user_id",
    [
        (1,1),
        (2,1),
        (11,2),
        (21,3)
    ]
)
def test_post_details(post_id,expected_user_id):
    resp=requests.get(f"{BASE_URL}/posts/{post_id}")
    data=resp.json()
    assert data["id"] == post_id
    assert data["userId"] == expected_user_id    

@pytest.mark.parametrize(
    ["user_id","title","body"],
    [
        (1, "Title 1", "Body 1"),
        (2, "Title 2", "Body 2"),
        (3, "Title 3", "Body 3")
    ]
)
def test_create_post(user_id,title,body):
    # when we send some data to endpoint it is called payload
    payload={"user_id":user_id, "title":title,"body":body}
    
    response = requests.post(f"{BASE_URL}/posts",
                         json=payload,
                         timeout=5
                         )
    # 2. field -- id field
    # 3. data that was sent
    data = response.json()
    assert response.status_code == 201
    assert "id" in data
    assert data["user_id"] == user_id
    assert data["title"] == title
    assert data["body"] == body

with open("test_data.json","r") as file:
    test_data=json.load(file)

def test_create_post_file(test_case):
    payload=test_case["payload"]
    expected_status=test_case["expected_status"]
    
    response = requests.post(f"{BASE_URL}/posts",
                             json=payload,
                             timeout=5
                             )
    data = response.json()
    assert response.status_code == expected_status
