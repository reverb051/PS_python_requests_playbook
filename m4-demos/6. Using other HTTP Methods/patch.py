import requests

response = requests.patch(
    "http://127.0.0.1:8000/api/items/1",
    json={"name": "Updated PATCH Name"}
)

print(response.json())