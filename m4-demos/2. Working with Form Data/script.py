import requests


response = requests.post(
    "http://127.0.0.1:8000/items/new",
    data={"name": "Another item", "price": 44},
    allow_redirects=False,
)
print(response.request.headers["content-type"])
print(response.request.body)