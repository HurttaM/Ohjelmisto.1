import requests
import json

vastaus = requests.get("https://api.chucknorris.io/jokes/random").json()
print(vastaus['value'])
