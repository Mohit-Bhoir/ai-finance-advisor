📊 AI-Driven Personal Finance Portfolio Advisor

An end-to-end AI-powered financial advisory platform that recommends ETF portfolios based on user risk appetite and capital, runs Monte-Carlo simulations, supports automated retraining pipelines, and generates advisory invoices — built with production-grade MLOps practices.

⚠️ Disclaimer:
This project is for illustrative and educational purposes only. Performance is not guaranteed and may not reflect real-world trading outcomes.

🚀 Features

📥 User risk & capital profiling

📊 Mean-Variance Portfolio Optimization (Efficient Frontier)

📈 Monte-Carlo scenario simulation

🎚️ Risk gauge + percentile visualizations

📉 Risk metrics (Sharpe, volatility, drawdown)

🔁 Retraining pipelines with DVC

📊 Experiment tracking with MLflow (DagsHub)

🧾 Advisory invoice generation (1% demo fee)

📄 PDF invoice download

🌐 Web dashboard built with FastAPI + HTML/CSS

🐳 Dockerized deployment


🧠 System Architecture
User Input
   ↓
Risk Profiler
   ↓
ML Return Model
   ↓
Portfolio Optimizer
   ↓
Monte Carlo Simulator
   ↓
Dashboard + Invoice Generator

🛠 Tech Stack

ML / Quant

Python, Pandas, NumPy

Scikit-learn

PyPortfolioOpt

Monte-Carlo Simulation

MLOps

DVC

MLflow

DagsHub

Drift Detection (Evidently)

Backend / UI

FastAPI

HTML + CSS

Matplotlib charts

ReportLab (PDF invoices)

Infra

Docker

📊 Dashboard Preview

Add screenshots here:

Home input form

Portfolio allocation pie

Monte-Carlo histogram

KPI cards

Invoice PDF download

🔁 Training & Retraining Pipeline

The entire ML workflow is tracked with DVC:

Market data ingestion

Cleaning & preprocessing

Feature engineering

Model training

Portfolio optimization

Evaluation

Drift detection & retraining

📄 Generate Invoice PDFs

Invoices are automatically generated when users submit the dashboard form.

They can also be downloaded via the UI.

⭐ Future Enhancements

Live rebalancing engine

Regime detection

Alternative asset classes

Cloud deployment

Authentication

Multi-user portfolios

📎 License

MIT
