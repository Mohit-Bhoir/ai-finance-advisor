import matplotlib.pyplot as plt
import io
import base64
import numpy as np


def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return encoded


def allocation_pie(weights: dict):
    labels = list(weights.keys())
    values = list(weights.values())

    fig, ax = plt.subplots(figsize=(7, 5))

    wedges, texts, autotexts = ax.pie(
        values,
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.8,
    )

    ax.legend(
        wedges,
        labels,
        title="Assets",
        loc="center left",
        bbox_to_anchor=(1.05, 0.5),
    )

    ax.set_title("Portfolio Allocation")

    return fig_to_base64(fig)



def monte_carlo_histogram(sim_results):
    fig, ax = plt.subplots()
    ax.hist(sim_results, bins=40)
    ax.set_title("Monte Carlo Terminal Wealth Distribution")
    ax.set_xlabel("Growth Multiple")
    ax.set_ylabel("Frequency")

    return fig_to_base64(fig)

def risk_gauge(volatility: float):
    # volatility expected ~0–0.3
    pct = min(volatility / 0.30, 1.0)

    fig, ax = plt.subplots(figsize=(6, 1.6))
    ax.barh([0], [1], color="#eee")
    ax.barh([0], [pct], color="#f29900")

    ax.set_xlim(0, 1)
    ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1])
    ax.set_xticklabels(["Low", "Medium", "High"])
    ax.set_title("Risk Level (Volatility Gauge)")

    return fig_to_base64(fig)


