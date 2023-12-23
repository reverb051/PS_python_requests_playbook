import requests

response = requests.put(
    "http://127.0.0.1:8000/api/items/1", 
    json={"name": "Updated PUT Name", "price": 100}
)

print(response.json())