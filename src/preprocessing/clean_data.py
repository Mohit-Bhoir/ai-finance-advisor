import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/market_prices.csv")
OUT_PATH = Path("data/processed/clean_prices.csv")

def main():
    df = pd.read_csv(RAW_PATH, index_col=0, parse_dates=True)

    # forward fill small gaps
    df = df.ffill()

    # drop remaining NaNs
    df = df.dropna()

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH)

    print("Saved:", OUT_PATH)

if __name__ == "__main__":
    main()
