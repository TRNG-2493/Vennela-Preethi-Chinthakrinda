import requests

BASE="https://api.example.com"

def get_user(user_id):
    r=requests.get(f"{BASE}/users/{user_id}",timeout=5)
    r.raise_for_status()
    return r.json()["name"]
# calls the endpoint and returns the name



    
    