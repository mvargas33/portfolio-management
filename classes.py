import json

class Portfolio:
  """
  Base class for every Portfolio.

  Parameters
  ----------
  stocks: list of Stock objetcs
    The list of stocks for this portfolio
  
  weights: list of float
    The weight of each Stock in the Portfolio

  name: str
    The name of the portfolio

  Observations
  ------------

  - The Portfolio is measured in USD
  - The are no transactions in the system. You create a Portfolio, you end with the same Stocks.
  - Weights are actually the percentage of participation of the portfolio at the start.
  - You can only see the consecuences of the initial Portfolio.
  """
  def __init__(self, stocks_symbols=[], weights=[], name="My portfolio") -> None:
    if len(stocks) != len(weights):
      raise Exception("The lenght of stocks must match the lenght of weight of each stock in the portfolio")
    if sum(weights) != 1.0:
      raise Exception("The sum of all weights must be 1.0")

    # Create Stock objects
    stocks = []
    for symbol in stocks_symbols:
      stocks.append(Stock(symbol=symbol))

    self.stocks = stocks
    self.weight = weights
    self.name = name

  """
  Return profits if the portfolio given two dates

  Parameters
  ----------
  
  date_from: string with the date in the ISO format "yyyy-mm-dd"
    Start date of the entire Portfolio
  
  date_to: string with the date in the ISO format "yyyy-mm-dd"
    End date

  Returns
  -------

  profit : float
    The simple profit of the portfolio between two dates
  annualized return : float
    The annualized return of the portfolio between two dates
  """
  def profit(self, date_from="", date_to=""):
    
    pass


class Stock:
  """
  Base class for every Stock

  Parameters
  ----------
  symbol: string
    The symbol of the stock. For intance "BTC" or "TSLA"
  """
  def __init__(self, symbol) -> None:
    self.symbol = symbol

  """
  Return the open and close prices of the stock given a date

  Parameters
  ----------
  
  date: string with the date in the ISO format "yyyy-mm-dd"
    Consulting date

  Returns
  -------

  open : float
    The open price of the stock in the date specified
  close : float
    The close price of the stock in the date specified
  """
  def price(self, date):
    with open(f'./fixtures/{self.symbol}.json') as json_file:
      data = json.load(json_file)
    return float(data[date]["open"]), float(data[date]["close"])