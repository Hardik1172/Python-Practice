import requests
api_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url)
if response.text == "":
    print("Response empty")
else:
    print("respnse", response.text)
