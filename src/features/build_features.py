import pandas as pd
from pathlib import Path

IN_PATH = Path("data/processed/clean_prices.csv")
OUT_PATH = Path("data/features/returns_features.csv")

def main():
    prices = pd.read_csv(IN_PATH, index_col=0, parse_dates=True)

    returns = prices.pct_change().dropna()

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    returns.to_csv(OUT_PATH)

    print("Saved:", OUT_PATH)

if __name__ == "__main__":
    main()
