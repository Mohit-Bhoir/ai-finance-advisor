import pandas as pd
from pathlib import Path
from pypfopt import EfficientFrontier, expected_returns, risk_models
import yaml
from src.recommender.universe_rules import allowed_assets

from src.recommender.capital_policy import capital_profile

PRICE_PATH = Path("data/processed/clean_prices.csv")


def optimize_portfolio(risk_level: str, capital: float):

    tickers = allowed_assets(capital, risk_level)

    prices = pd.read_csv(PRICE_PATH, index_col=0)

    prices = prices[tickers]   # FILTER HERE 🔥

    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)

    policy = capital_profile(capital)

    base_vol = {
        "low": 0.08,
        "medium": 0.15,
        "high": 0.25,
    }[risk_level]

    target_vol = base_vol * policy["risk_scale"]

    ef = EfficientFrontier(mu, S)

    ef.efficient_risk(target_vol)

    cleaned = ef.clean_weights()
    perf = ef.portfolio_performance(verbose=False)

    return cleaned, perf

