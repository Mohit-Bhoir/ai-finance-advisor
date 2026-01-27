import pandas as pd
from pathlib import Path
from pypfopt import EfficientFrontier, expected_returns, risk_models
import yaml

PRICE_PATH = Path("data/processed/clean_prices.csv")

def load_params():
    with open("params.yaml") as f:
        return yaml.safe_load(f)

def optimize_portfolio(risk_level: str):
    prices = pd.read_csv(PRICE_PATH, index_col=0)

    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)

    ef = EfficientFrontier(mu, S)

    if risk_level == "low":
        weights = ef.min_volatility()
    elif risk_level == "high":
        weights = ef.max_sharpe()
    else:
        weights = ef.efficient_risk(target_volatility=0.15)

    cleaned = ef.clean_weights()
    perf = ef.portfolio_performance(verbose=False)

    return cleaned, perf
