import yfinance as yf
import pandas as pd
import yaml
from pathlib import Path

DATA_DIR = Path("data/raw")

def load_params():
    with open("params.yaml") as f:
        return yaml.safe_load(f)

def fetch_data(tickers, start):
    data = yf.download(tickers, start=start, group_by="ticker")
    prices = pd.DataFrame()

    for t in tickers:
        prices[t] = data[t]["Close"]

    return prices.dropna()

def main():
    params = load_params()
    tickers = params["data"]["tickers"]
    start_date = params["data"]["start_date"]

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    df = fetch_data(tickers, start_date)
    df.to_csv(DATA_DIR / "market_prices.csv")

    print("Saved data/raw/market_prices.csv")

if __name__ == "__main__":
    main()
