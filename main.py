from classes.classes import Portfolio
from fixtures.fixtures import gen_fixtures


def test_simple_portfolio():
  start_date = "2020-01-06"
  end_date = "2022-01-06"
  verbose = True

  # Portfolios
  btc_portfolio = Portfolio(name="Bitcoin portfolio", stocks_symbols=["BTC"], stocks_weights=[1], verbose=verbose)
  crypto_portfolio = Portfolio(name="Crypto portfolio", stocks_symbols=["BTC", "ETH", "LINK"], stocks_weights=[0.3, 0.5, 0.2], verbose=verbose)
  stocks_portfolio = Portfolio(name="Stocks portfolio", stocks_symbols=["TSLA", "AAPL", "AMZN", "MSFT"], stocks_weights=[0.25, 0.25, 0.25, 0.25], verbose=verbose)
  mixed_portfolio = Portfolio(name="Mixed  portfolio", stocks_symbols=["AMZN", "IBM", "BTC", "DOGE"], stocks_weights=[0.3, 0.2, 0.3, 0.2], verbose=verbose)

  portfolios = [btc_portfolio, crypto_portfolio, stocks_portfolio, mixed_portfolio]

  for portfolio in portfolios:
    profit, annualized_return = portfolio.profit(start_date, end_date)
    print(f"\n{portfolio.name} \t| Profit:  {profit*100:.2f} % \t| Annualized return: {annualized_return*100:.2f} %")

if __name__ == "__main__":
    # gen_fixtures()
    test_simple_portfolio()