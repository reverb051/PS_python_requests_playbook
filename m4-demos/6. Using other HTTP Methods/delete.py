import requests

response = requests.delete(
    "http://127.0.0.1:8000/api/items/0",
)

print(response.json())