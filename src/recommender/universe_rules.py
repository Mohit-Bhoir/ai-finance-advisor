ALL_ASSETS = {
    "index": ["VTI", "VOO"],
    "equity": ["AAPL", "MSFT", "GOOGL", "AMZN"],
    "bond": ["AGG"],
    "hedge": ["GLD"],
}

CAPITAL_TIERS = {
    "small": ["index", "bond", "hedge"],
    "mid": ["index", "bond", "equity"],
    "large": ["index", "bond", "equity", "hedge"],
}

RISK_FILTERS = {
    "low": ["index", "bond", "hedge"],
    "medium": ["index", "bond", "equity"],
    "high": ["index", "equity"],
}


def capital_bucket(capital: float):
    if capital < 500:
        return "small"
    elif capital < 5000:
        return "mid"
    return "large"


def allowed_assets(capital: float, risk: str):

    tier = capital_bucket(capital)

    cap_groups = set(CAPITAL_TIERS[tier])
    risk_groups = set(RISK_FILTERS[risk])

    groups = cap_groups.intersection(risk_groups)

    tickers = []
    for g in groups:
        tickers.extend(ALL_ASSETS[g])

    return sorted(set(tickers))
