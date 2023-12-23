import requests

message_body = {"name": "Some item", "price": 22}

response = requests.post(
    "http://127.0.0.1:8000/api/items",
    json=message_body
)

print(response.request.headers["content-type"])
print(response.request.body)