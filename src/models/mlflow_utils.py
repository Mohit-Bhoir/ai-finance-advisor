import mlflow
import os

def setup_mlflow():
    uri = os.getenv("MLFLOW_TRACKING_URI")
    if uri:
        mlflow.set_tracking_uri(uri)

    mlflow.set_experiment("ai-finance-advisor")
