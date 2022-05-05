# Overview

This repo allows users to simulate a custom portfolio, with US stocks and crypto. You buy stocks once, and see the performace of it until a specific date. Portfolio is measured in USD. No tax nor inflation. is considered.

Create and simulate your portfolio inside the `main.py` file.

The repo has already some stocks to play with: AAPL, ADA, AMZN, BTC, DOGE, ETH, IBM, LINK, MSFT, TSLA, XLM (last update 2022-05-04)

# Instructions

- Install python 3
- Create a python 3 virtual environment with `python3 -m venv venv`
- Source the environment. For windows use `.\venv\scripts\activate`. For linux use `source ./bin/activate`
- Install dependencies with `pip3 install -r requirements.txt`
- Run the examples with `python3 main.py`

# Update or add stocks

- Get a public, free-to-use API key from Alphavantage [https://www.alphavantage.co](here)
- Create a .env file in the root directory and add the following line `ALPHAVANTAGE_API_KEY=XXXXXXXXXXXXXX`
- To add stocks, update the list inside the function `gen_fixtures` at `fixtures/fixtures.py`. See stocks available in the [https://www.alphavantage.co](site).
- To fetch stock prices, uncomment the function `gen_fixtures` inside `main` function

# Package files and directories

- `main.py` run a simulation with three different portfolios
- `test.py` run a handmade example that checks the behaviour of profit and annualized return functions
- `classes/` contains the `Portfolio` and `Stock` classes.
- `fixtures/` contains the files to manage the stocks data wth the public API.

# Notes

- Some stocks only have data since 2020. The script may fail if you use older dates.
- This repo is not professional. Further testing is needed and has a lot of limitations.