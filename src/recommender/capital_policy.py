def capital_profile(capital: float):

    if capital < 500:
        return {
            "max_assets": 3,
            "cash_buffer": 0.20,
            "risk_scale": 0.7,
        }

    elif capital < 5000:
        return {
            "max_assets": 4,
            "cash_buffer": 0.10,
            "risk_scale": 0.9,
        }

    else:
        return {
            "max_assets": 6,
            "cash_buffer": 0.05,
            "risk_scale": 1.05,
        }
