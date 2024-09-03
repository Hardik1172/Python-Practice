import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo'



params = {
             'Time Series (5min)': '2024-07-08 19:15:00'
}

response = requests.get(url, params = params)
if response.text == "":
    print("wrong content")
else:
    print("response:", response.text)

