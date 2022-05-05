import json, os
from datetime import datetime

class Portfolio:
  """
  Base class for every Portfolio.

  Parameters
  ----------
  stocks_symbols: list of Stock objetcs
    The list of stocks for this portfolio
  
  stocks_weights: list of float
    The weight of each Stock in the Portfolio

  name: str
    The name of the portfolio
  
  verbose: bool
    Use True to print the weighted return of each stock

  Observations
  ------------

  - The Portfolio is measured in USD
  - The are no transactions in the system. You create a Portfolio, you end with the same Stocks.
  - Weights are actually the percentage of participation of the portfolio at the start.
  - You can only see the consecuences of the initial Portfolio.
  """
  def __init__(self, stocks_symbols=[], stocks_weights=[], name="My portfolio", verbose=False) -> None:
    if len(stocks_symbols) != len(stocks_weights):
      raise Exception("The lenght of stocks must match the lenght of weight of each stock in the portfolio")
    if sum(stocks_weights) != 1.0:
      raise Exception("The sum of all stocks weights must be 1.0")

    self.stocks = [Stock(symbol=stock_symbol) for stock_symbol in stocks_symbols]  # Create Stock objects
    self.stocks_weights = zip(self.stocks, stocks_weights)  # Pair with weight
    self.name = name
    self.verbose = verbose

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
    days = abs((datetime.strptime(date_to, "%Y-%m-%d") - datetime.strptime(date_from, "%Y-%m-%d")).days)
    accum_profit = 0

    if self.verbose:
      print(f'\nSymbol \t| Intial price \t| Final price \t| Variation (%)\t| Position (%) \t| Return \t| Cum. Return')
      print(f'------------------------------------------------------------------------------------------------------')

    for element in self.stocks_weights:
      stock, weight = element
      initial_price = stock.price(date=date_from)[0]  # Open price
      final_price = stock.price(date=date_to)[1]  # Close price

      accum_profit += weight * ((final_price/initial_price) - 1)
      if self.verbose:
        print(f'{stock.symbol} \t| {initial_price:.4f} \t| {final_price:.4f} \t| {((final_price/initial_price) - 1)*100:.4f} \t| {weight:.4f} \t| { weight * ((final_price/initial_price) - 1):.4f} \t| {accum_profit:.4f}')
    
    return accum_profit, (1 + accum_profit)**(365/days) - 1


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
    with open(os.path.join(os.path.abspath(os.getcwd()), "fixtures", "data", f'{self.symbol}.json')) as json_file:
      data = json.load(json_file)
    try:
      return float(data[date]["open"]), float(data[date]["close"])
    except KeyError:
      raise Exception(f"The stock {self.symbol} does not have activity on the date {date}. Try another date")