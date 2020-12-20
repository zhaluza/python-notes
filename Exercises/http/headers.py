import requests

url = "https://icanhazdadjoke.com/"

# Plain text response
# text_res = requests.get(url, headers={"Accept": "text/plain"})

res = requests.get(url, headers={"Accept": "application/json"})
data = res.json()

print(res.text)
print(data["joke"])