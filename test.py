import os, json
from datetime import datetime
from classes.classes import Portfolio

current_path = os.path.dirname(os.path.abspath(__file__))

"""
Loads handmade exaples to the system.
"""
def load_example():
  custom_stock_A = {
    "2022-05-04": {"open": "2.8", "close": "2.9"},
    "2021-05-01": {"open": "1.0", "close": "1.2"}
  }

  custom_stock_B = {
    "2022-05-04": {"open": "1.1", "close": "1.0"},
    "2021-05-01": {"open": "10.0", "close": "12.7"}
  }

  with open(os.path.join(current_path, "fixtures", "data", f'STOCKA.json'), 'w') as outfile:
    json.dump(custom_stock_A, outfile)

  with open(os.path.join(current_path, "fixtures", "data", f'STOCKB.json'), 'w') as outfile:
    json.dump(custom_stock_B, outfile)

"""
Deletes the handmade examples from the system.
"""
def delete_example():
  os.remove(os.path.join(current_path, "fixtures", "data", f'STOCKA.json'))
  os.remove(os.path.join(current_path, "fixtures", "data", f'STOCKB.json'))


"""
Test the results of the profit() function for a handmade example.
"""
def test_handmade_example():
  start_date = "2021-05-01"
  end_date = "2022-05-04"
  days_passed = abs((datetime.strptime(start_date, "%Y-%m-%d") - datetime.strptime(end_date, "%Y-%m-%d")).days)
  verbose = True

  my_portfolio = Portfolio(name="My portfolio", stocks_symbols=["STOCKA", "STOCKB"], stocks_weights=[0.2, 0.8], verbose=verbose)
  profit, annualized_return = my_portfolio.profit(start_date, end_date)
  print(f"Profit:  {profit*100:.2f} % \t| Annualized return: {annualized_return*100:.2f} %")

  # Compare results
  expected_profit = (0.2*(2.9/1.0 - 1)) + (0.8*(1.0/10.0 - 1))
  assert profit == expected_profit
  assert annualized_return == (1 + expected_profit)**(365/days_passed) - 1
  print("All tests passed.")

if __name__ == "__main__":
  load_example()
  test_handmade_example()
  delete_example()