import requests
import xml.etree.ElementTree as ET

message_body = """
<item>
    <name>Some item</name>
    <price>300</price>
</item>
"""

response = requests.post(
    "http://127.0.0.1:8000/api/items/xml",
    data=message_body, 
    headers={"Content-Type": "application/xml"}
)

# print(response.text)
print(ET.fromstring(response.text).find("name").text)
print(ET.fromstring(response.text).find("price").text)