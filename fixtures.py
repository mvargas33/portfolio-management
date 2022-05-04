import json, requests, os
from dotenv import load_dotenv

load_dotenv() # Load loacl env for API Key

"""
Gets the historical data prices for the specified symbol.
currency_type can de "crypto" or "stock".
"""
def get_hitorical_ticker(symbol="AAPL", currency_type="stock"):
  if currency_type == "crypto":
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=USD&apikey={os.getenv("ALPHAVANTAGE_API_KEY")}'
    r = requests.get(url)
    data = r.json()
    simplified = {}
    for key in data['Time Series (Digital Currency Daily)'].keys():
      point = {
        "open": data['Time Series (Digital Currency Daily)'][key]['1a. open (USD)'],
        "close": data['Time Series (Digital Currency Daily)'][key]['4a. close (USD)']
      }
      simplified[key] = point

    with open(f'./fixtures/{symbol}.json', 'w') as outfile:
      json.dump(simplified, outfile)


  elif currency_type == "stock":
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={os.getenv("ALPHAVANTAGE_API_KEY")}'
    r = requests.get(url)
    data = r.json()
    simplified = {}
    for key in data['Time Series (Daily)'].keys():
      point = {
        "open": data['Time Series (Daily)'][key]['1. open'],
        "close": data['Time Series (Daily)'][key]['4. close']
      }
      simplified[key] = point

    with open(f'./fixtures/{symbol}.json', 'w') as outfile:
      json.dump(simplified, outfile)

"""
Generates the base fixtures for the system.
"""
def gen_fixtures():
  stocks_list = [
    ("BTC", "crypto"),
    ("ETH", "crypto"),
    ("LINK", "crypto"),
    ("ADA", "crypto"),
    ("DOGE", "crypto"),
    ("XLM", "crypto"),
    ("TSLA", "stock"),
    ("AAPL", "stock"),
    ("IBM", "stock"),
    ("MSFT", "stock"),
    ("AMZN", "stock")
  ]

  for pair in stocks_list:
      get_hitorical_ticker(symbol=pair[0], currency_type=pair[1])