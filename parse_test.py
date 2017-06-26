import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")
data = json.loads(r.text)
print (data[0]["id"])

