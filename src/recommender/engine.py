from src.optimization.portfolio_optimizer import optimize_portfolio
from src.simulation.monte_carlo import simulate
from src.recommender.capital_policy import capital_profile


def recommend(risk_level: str, capital: float):

    policy = capital_profile(capital)

    weights, perf = optimize_portfolio(
        risk_level=risk_level,
        capital=capital,
    )

    sim = simulate(weights)

    return {
        "weights": weights,
        "expected_return": perf[0],
        "volatility": perf[1],
        "sharpe": perf[2],
        "simulation": sim,
        "recommended_capital": capital,
        "capital_policy": policy,
    }
