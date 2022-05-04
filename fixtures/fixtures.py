import json, requests, os, time
from dotenv import load_dotenv

load_dotenv() # Load loacl env for API Key
path = os.path.dirname(os.path.abspath(__file__))

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

    with open(os.path.join(path, "data", f'{symbol}.json'), 'w') as outfile:
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

    with open(os.path.join(path, "data", f'{symbol}.json'), 'w') as outfile:
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
    ("TSLA", "stock"),
    ("AAPL", "stock"),
    ("IBM", "stock"),
    ("MSFT", "stock"),
    ("AMZN", "stock")
  ]

  print(f"Fetching the following stocks from a public API: {' '.join([e[0] for e in stocks_list])}")
  for i, pair in enumerate(stocks_list):
    if i % 5 == 0 and i > 0:  # 5 calls per minute
      print("Waiting 1 minute because of the API limitations ...")
      time.sleep(65)
    get_hitorical_ticker(symbol=pair[0], currency_type=pair[1])