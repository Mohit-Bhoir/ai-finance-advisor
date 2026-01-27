import pandas as pd
from pathlib import Path

from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

REF_PATH = Path("data/features/returns_features.csv")

def run_drift(new_data_path: str):
    reference = pd.read_csv(REF_PATH)
    current = pd.read_csv(new_data_path)

    dashboard = Dashboard(tabs=[DataDriftTab()])
    dashboard.calculate(reference_data=reference, current_data=current)

    dashboard.save("drift_report.html")

    print("Saved drift_report.html")

if __name__ == "__main__":
    run_drift("data/features/returns_features.csv")
