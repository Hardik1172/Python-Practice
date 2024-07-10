import requests

URL = "https://www.indiatoday.in/headlines"

response = requests.get(URL)

if response.text == "":
    print("sorry it is empty")

else:
    print(response.json())





