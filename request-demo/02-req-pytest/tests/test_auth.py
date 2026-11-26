import requests as req
from requests.auth import HTTPBasicAuth
import os

HB="https://httpbin.org"


def test_basic_auth_success():
    resp=req.get(f"{HB}/basic-auth/user/passwd",
                 auth=HTTPBasicAuth("user","passwd"),
                 timeout=10
                 )
    assert resp.status_code==200
    
    assert resp.json()=={"authenticated":True,
                         "user":"user",
                         "authorized":True}

def test_basic_auth_wrong_pass():
    resp=req.get(f"{HB}/basic-auth/user/passwd",
                 auth=HTTPBasicAuth("user","wrong"),
                 timeout=10
                 )
    assert resp.status_code==401
    
# token are always stored in env variables

TOKEN = os.getenv("API_TOKEN","dev-token-123")

def test_bearer_token():
    s=req.Session()
    s.headers.update({"Authorization":f"Bearer {TOKEN}"})
    resp=s.get(f"{HB}/bearer",timeout=10)
    
    assert resp.status_code==200

