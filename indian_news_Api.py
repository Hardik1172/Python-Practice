import requests

url = 'https://www.indiatoday.in/'


response = requests.get(url)

if response.text == "":
    print("wrong content")
else:
    print("response:", response.text)

