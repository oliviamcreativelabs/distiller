from . import requests

url = "https://the-cocktail-db.p.rapidapi.com/list.php"

querystring = {"a": "list"}

headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "b8a6c912e5msh8577bad2b77e723p115961jsnbe7c9190c1a1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
