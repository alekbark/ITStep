import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
data = response.json()

with open("post.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

