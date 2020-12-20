import requests

url = "https://icanhazdadjoke.com/search"
params = {"term": "cat"}

res = requests.get(url, headers={"Accept": "application/json"}, params=params)
data = res.json()

print(data["results"])