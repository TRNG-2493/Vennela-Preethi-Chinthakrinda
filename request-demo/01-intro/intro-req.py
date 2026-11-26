import requests

BASE_URL= "https://jsonplaceholder.typicode.com/"

response=requests.get(f"{BASE_URL}/posts/1", timeout=5);

print(response.status_code, response.reason)

print(response.headers["Content-Type"])

post=response.json()
print(post)
print(post["title"])

r=requests.get(f"{BASE_URL}/posts",params={"userId":2},timeout=5)
print(r.url)

# dynamic path variable
post_id=1
response=requests.get(f"{BASE_URL}/posts/{post_id}", timeout=5);

# send data to server using POST method and send data as JSON
print("="*40)
post_data=requests.post(f"{BASE_URL}/posts",
                        json={"title":"my title", "body":"hello", "userId": 1}, 
                        timeout=5
                        )
print(post_data.status_code,post_data.json())

print("*"*75)
try:
    r=requests.get(f"{BASE_URL}/posts/9999",timeout=5)
    r.raise_for_status()
except requests.HTTPError as e:
    print("HTTP Error: ",e)
    
