import requests

url  = "https://example.com"

response = requests.get(url)

with open("file.html", "w",encoding="utf-8") as file:
    file.write(response.text)

print("Html File Saved Successfully")
