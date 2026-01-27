<<<<<<< HEAD
# 📊 AI-Driven Personal Finance Portfolio Advisor

An end-to-end **AI-powered financial advisory platform** that recommendsETF portfolios based on user risk appetite and capital, runs Monte-Carlosimulations, supports automated retraining pipelines, and generatesadvisory invoices --- built using **production-grade MLOps practices**.

> ⚠️ **Disclaimer**  
> This portfolio advisor engine is for illustrative and educationalpurposes only.  
> Performance is not guaranteed to be optimal or representative ofreal-world trading results.  
> Use at your own risk.

---

## 🚀 Features

-   📥 User risk & capital profiling
-   📊 Mean-Variance Portfolio Optimization (Efficient Frontier)
-   📈 Monte-Carlo scenario simulation
-   🎚️ Risk gauge meter
-   📉 Risk metrics (Sharpe ratio, volatility, drawdown)
-   📊 Percentile growth visualizations
-   🔁 Retraining pipelines with DVC
-   📊 Experiment tracking with MLflow (DagsHub)
-   📉 Drift monitoring
-   🧾 Advisory invoice generation (1% demo fee)
-   📄 Downloadable PDF invoices
-   🌐 Web dashboard built with FastAPI + HTML/CSS
-   🐳 Dockerized deployment

---

## 🧠 System Architecture

```
User Input   ↓Risk Profiler   ↓ML Return Model   ↓Portfolio Optimizer   ↓Monte-Carlo Simulator   ↓Dashboard + Invoice Generator
```
=======
📊 AI-Driven Personal Finance Portfolio Advisor

An end-to-end AI-powered financial advisory platform that recommends ETF portfolios based on user risk appetite and capital, runs Monte-Carlo simulations, supports automated retraining pipelines, and generates advisory invoices — built with production-grade MLOps practices.

⚠️ Disclaimer:
This project is for illustrative and educational purposes only. Performance is not guaranteed and may not reflect real-world trading outcomes.
>>>>>>> 896fd9bc8a120f504c74ef83be43307a1c1f4923

---

<<<<<<< HEAD
## 🛠 Tech Stack

### Quant / ML

-   Python
-   Pandas / NumPy
-   Scikit-learn
-   PyPortfolioOpt
-   Monte-Carlo Simulation

### MLOps

-   DVC
-   MLflow
-   DagsHub
-   Evidently (drift detection)

### Backend / UI

-   FastAPI
-   HTML + CSS
-   Matplotlib charts
-   ReportLab (PDF invoices)

### Infrastructure

-   Docker

---

## 📊 Dashboard Preview

*Add screenshots here:*
=======
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
>>>>>>> 896fd9bc8a120f504c74ef83be43307a1c1f4923

-   Home input form
-   Portfolio allocation pie chart
-   Monte-Carlo distribution histogram
-   KPI cards
-   Risk gauge meter
-   Invoice PDF download

---

## 🔁 Training & Retraining Pipeline

<<<<<<< HEAD
The entire ML workflow is tracked with **DVC**:

1.  Market data ingestion
2.  Cleaning & preprocessing
3.  Feature engineering
4.  Model training
5.  Portfolio optimization
6.  Evaluation & backtesting
7.  Drift detection & retraining

Run the full pipeline:

```bash
dvc repro
```

---

## 🐳 Run Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Run ML pipeline

```bash
dvc repro
```

---

### 3️⃣ Start API server

```bash
uvicorn src.api.main:app --reload
```

Open in browser:

👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📄 Invoice PDFs

Invoices are generated automatically after portfolio recommendations.

Users can download them directly from the dashboard.

---

## 📉 Drift Monitoring

Generate drift reports:

```bash
python src/retraining/drift_detector.py
```

This creates:

```
drift_report.html
```

---

## 🐳 Docker

Build image:

```bash
docker build -t ai-finance-advisor .
```

Run container:

```bash
docker run -p 8000:8000 ai-finance-advisor
```

---

## 💼 Why This Project Matters

This system demonstrates:

-   production-grade ML pipelines
-   quantitative finance modeling
-   retraining & monitoring
-   API deployment
-   visualization dashboards
-   SaaS-style billing simulation
-   product-driven engineering

Designed for **AI/ML Engineer** and **FinTech / Quantitative Finance**roles.

---

## ⭐ Future Enhancements

-   Regime detection
-   Dynamic rebalancing
-   Additional asset classes
-   Cloud deployment
-   Authentication
-   Multi-user portfolios

---

## 📜 License
=======
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
>>>>>>> 896fd9bc8a120f504c74ef83be43307a1c1f4923

MIT

---

## 🧾 CV Header Version

**AI-Driven Personal Finance Portfolio Advisor** --- *Python, FastAPI,DVC, MLflow, PyPortfolioOpt, Docker*  
Built a production-style AI finance platform that optimizes ETFportfolios, runs Monte-Carlo simulations, supports retraining pipelineswith drift monitoring, and provides a web dashboard with automatedinvoice generation.