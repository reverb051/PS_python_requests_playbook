import requests

file1 = open("file1.csv", "rb")
file2 = open("file2.csv", "rb")
files = [
    ("files", ("file1.csv", file1, "text/csv")),
    ("files", ("file2.csv", file2, "text/csv")),
]
# files = {"file": open("file1.csv", "rb")}


response = requests.post(
    "http://127.0.0.1:8000/upload-files",
    files=files,
)

file1.close()
file2.close()

print(response.json())