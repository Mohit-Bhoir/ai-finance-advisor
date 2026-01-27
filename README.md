📊 AI-Driven Personal Finance Advisor

An end-to-end data-driven financial portfolio recommendation system that:

Accepts user inputs (salary, risk appetite, goals)

Predicts expected returns & risk

Optimizes asset allocation

Runs Monte-Carlo simulations

Retrains models periodically using DVC pipelines

Tracks experiments with MLflow (DagsHub)

Generates monthly advisory invoices (1% of recommended capital)

🚀 Features

Portfolio optimization (Modern Portfolio Theory)

ML return prediction

Risk profiling engine

Automated retraining

Model drift detection (planned)

Invoice generator module

REST API

React dashboard (planned)

🏗️ Architecture
User Input → Risk Profiler → Return Model → Optimizer → Simulator
                     ↓
                  Invoice Engine

🛠️ Tech Stack

Python

FastAPI

DVC

MLflow

DagsHub

Pandas / NumPy / Scikit-learn

PyPortfolioOpt

React + Tailwind

🔁 Training Pipeline

Tracked with DVC:

Ingest Market Data

Clean & Preprocess

Feature Engineering

Train Models

Portfolio Optimization

Evaluation

📦 Setup
pip install -r requirements.txt
dvc pull

📜 License

MIT
