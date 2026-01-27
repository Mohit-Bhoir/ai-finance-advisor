import pandas as pd
import numpy as np
from pathlib import Path

FEATURE_PATH = Path("data/features/returns_features.csv")

def backtest(weights: dict):
    returns = pd.read_csv(FEATURE_PATH, index_col=0)

    w = np.array([weights[c] for c in returns.columns])

    portfolio_returns = returns @ w

    cumulative = (1 + portfolio_returns).cumprod()

    sharpe = portfolio_returns.mean() / portfolio_returns.std() * np.sqrt(252)
    max_dd = ((cumulative / cumulative.cummax()) - 1).min()

    return {
        "sharpe": sharpe,
        "max_drawdown": max_dd,
        "total_return": cumulative.iloc[-1] - 1
    }
