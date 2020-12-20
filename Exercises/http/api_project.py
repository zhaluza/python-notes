from pyfiglet import figlet_format
from termcolor import colored
import requests
import random

url = "https://icanhazdadjoke.com/search"

msg = "Dad Jokes : ("
welcome_text = figlet_format(msg)
welcome_text_formatted = colored(welcome_text, color="magenta")
print(welcome_text_formatted)


search_term = input("Search for a dad joke on any term:")
print(f"Looking for dad jokes on {search_term}")

params = {"term": search_term}

res = requests.get(url, headers={"Accept": "application/json"}, params=params)
data = res.json()
results = data["results"]
count = len(results)
if (count == 0):
    print(f"Sorry, I couldn't find any jokes about {search_term}! Please try again.")
else:  
    random_joke = colored(random.choice(results)["joke"], color="blue")

    print(f"I found {count} jokes about '{search_term}'!")
    print(f"Here's one: {random_joke}")