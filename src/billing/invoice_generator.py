from datetime import date
import uuid
import yaml

def load_fee():
    with open("params.yaml") as f:
        return yaml.safe_load(f)["billing"]["fee_rate"]

def generate_invoice(user_id: str, recommended_capital: float):
    fee_rate = load_fee()
    fee = round(recommended_capital * fee_rate, 2)

    return {
        "invoice_id": str(uuid.uuid4()),
        "user_id": user_id,
        "issue_date": date.today().isoformat(),
        "recommended_investment": recommended_capital,
        "monthly_fee": fee,
        "currency": "GBP",
        "status": "demo"
    }
