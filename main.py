from .classes import Portfolio
from .fixtures import gen_fixtures


def test_simple_portfolio():
  start_date = "2017-01-01"
  end_date = "2022-04-04"

  # Portfolios
  crypto_portfolio = Portfolio(name="Crypto portfolio", stocks=["BTC", "ETH", "LINNK"], weights=[0.3, 0.5, 0.2])
  stocks_portfolio = Portfolio(name="Stocks portfolio", stocks=["TSLA", "AAPL", "AMZN", "MSFT"], weights=[0.25, 0.25, 0.25, 0.25])
  mixed_portfolio = Portfolio(name="Mixed portfolio", stocks=["AMZN", "IBM", "BTC", "DOGE"], weights=[0.3, 0.2, 0.3, 0.2])

  portfolios = [crypto_portfolio, stocks_portfolio, mixed_portfolio]

  for portfolio in portfolios:
    profit, annualized_return = portfolio.profit(start_date, end_date)
    print(f"Profits from {portfolio.name}: {profit} | {annualized_return}")

if __name__ == "__main__":
    gen_fixtures()
    # test_simple_portfolio()