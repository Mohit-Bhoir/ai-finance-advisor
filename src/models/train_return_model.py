import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import yaml
import mlflow

from mlflow_utils import setup_mlflow

FEATURE_PATH = Path("data/features/returns_features.csv")
MODEL_PATH = Path("models/return_model.pkl")

def load_params():
    with open("params.yaml") as f:
        return yaml.safe_load(f)

def main():
    setup_mlflow()
    params = load_params()["training"]


    df = pd.read_csv(FEATURE_PATH)
    if 'Date' in df.columns:
        df = df.drop(columns=['Date'])

    X = df.shift(1).dropna()
    y = df.loc[X.index]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=params["test_size"], random_state=params["random_state"]
    )

    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=200, random_state=42)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)

        mlflow.log_param("model", "RandomForest")
        mlflow.log_metric("mse", mse)

        MODEL_PATH.parent.mkdir(exist_ok=True)
        joblib.dump(model, MODEL_PATH)

        print("Model saved:", MODEL_PATH)
        print("MSE:", mse)

if __name__ == "__main__":
    main()
