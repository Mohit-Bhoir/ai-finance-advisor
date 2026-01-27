import numpy as np
import pandas as pd
from pathlib import Path

PRICE_PATH = Path("data/processed/clean_prices.csv")

def simulate(weights: dict, n_years=10, n_sims=1000):
    prices = pd.read_csv(PRICE_PATH, index_col=0)
    returns = prices.pct_change().dropna()

    mu = returns.mean()
    cov = returns.cov()

    w = np.array([weights[k] for k in returns.columns])

    results = []

    for _ in range(n_sims):
        yearly = np.random.multivariate_normal(mu, cov, n_years * 252)
        portfolio = yearly @ w
        growth = np.cumprod(1 + portfolio)
        results.append(growth[-1])

    results = np.array(results)

    return {
        "raw": results.tolist(),
        "pct5": float(np.percentile(results, 5)),
        "median": float(np.percentile(results, 50)),
        "pct95": float(np.percentile(results, 95)),
    }
