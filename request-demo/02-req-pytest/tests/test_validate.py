import pytest
import requests
from jsonschema import validate

BASE_URL= "https://jsonplaceholder.typicode.com"

# send data - request schema
# receiving data - response schema
request_schema={
   "type":"object",
   "properties":{
      "title":{"type":"string"},
      "body":{"type":"string"},
      "userId":{
         "type":"integer",
         "minimum":1
      }
   },
   "required":["title","body","userId"],
   "additionalProperties":False
}
response_schema={
   "type":"object",
   "properties":{
      "id":{"type":"integer"},
      "title":{"type":"string"},
      "body":{"type":"string"},
      "userId":{"type":"integer"}
   },
   "required":["id","title","body","userId"],
   "additionalProperties":False
}

def test_create_post():
    payload={
        "title":"Testing POST",
        "body":"Body for POST",
        "userId":1
    }
    
    validate(instance=payload,schema=request_schema)
    
    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=5
    )
    
    assert response.status_code==201
    
    response_data=response.json();
    
    validate(instance=response_data,schema=response_schema)
    
    assert response_data["title"]==payload["title"]
    
    
    
    