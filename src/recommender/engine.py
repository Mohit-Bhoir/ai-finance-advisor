from src.optimization.portfolio_optimizer import optimize_portfolio
from src.simulation.monte_carlo import simulate


def recommend(risk_level: str, capital: float):
    weights, perf = optimize_portfolio(risk_level)

    sim = simulate(weights)

    return {
        "weights": weights,
        "expected_return": perf[0],
        "volatility": perf[1],
        "sharpe": perf[2],
        "simulation": sim,
        "recommended_capital": capital,
    }
