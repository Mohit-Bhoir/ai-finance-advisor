from fastapi import FastAPI, Request, background
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.responses import FileResponse
from src.billing.pdf_invoice import create_invoice_pdf



from src.recommender.engine import recommend
from src.billing.invoice_generator import generate_invoice

from src.api.plots import (
    allocation_pie,
    monte_carlo_histogram,
    risk_gauge,
)



from src.api.plots import allocation_pie, monte_carlo_histogram


app = FastAPI(title="AI Finance Advisor")

# -----------------------------
# API schema
# -----------------------------

class UserInput(BaseModel):
    user_id: str
    risk: str
    monthly_capital: float

# -----------------------------
# API endpoint
# -----------------------------

DISCLAIMER_HTML = """
<div class="disclaimer">
⚠️ <b>Disclaimer:</b> This portfolio advisor engine is for illustrative and educational purposes only.
The performance is not guaranteed to be optimal or representative of real-world trading results.
Use at your own risk.
</div>
"""

@app.post("/advise")
def advise(user: UserInput):
    advice = recommend(user.risk, user.monthly_capital)

    invoice = generate_invoice(
        user.user_id,
        advice["recommended_capital"]
    )

    return {
        "advice": advice,
        "invoice": invoice
    }

# -----------------------------
# Simple HTML dashboard
# -----------------------------

@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
            <html>
        <head>
        <title>AI Finance Advisor</title>

        <style>
        body {{
            font-family: system-ui;
            background: linear-gradient(135deg,#eef3ff,#ffffff);
        }}

        .card {{
            max-width: 520px;
            margin: 80px auto;
            background: white;
            padding: 40px;
            border-radius: 18px;
            box-shadow: 0 8px 40px rgba(0,0,0,0.08);
        }}

        .disclaimer {{
        background: #fff4e5;
        border-left: 6px solid #f29900;
        padding: 12px 18px;
        margin-bottom: 20px;
        border-radius: 10px;
        font-size: 14px;
        color: #663c00;
    }}

        
        input, select {{
            width: 100%;
            padding: 12px;
            margin-top: 6px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }}

        button {{
            background: #4285f4;
            color: white;
            padding: 14px;
            width: 100%;
            border-radius: 10px;
            border: none;
            font-size: 16px;
        }}
        </style>
        </head>

        <body>
        {DISCLAIMER_HTML}
        
        <div class="card">
        <h1>📊 AI Finance Advisor</h1>
        <p>Get personalized portfolio advice in seconds.</p>

        <form method="post" action="/ui">

        <label>Your Name</label>
        <input name="user_id" required>

        <label>Risk Level</label>
        <select name="risk">
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
        </select>

        <label>Monthly Capital (£)</label>
        <input type="number" name="capital" step="0.01" required>

        <button type="submit">Generate Recommendation</button>

        </form>
        </div>

        </body>
        </html>

    """

@app.post("/ui", response_class=HTMLResponse)
async def ui_submit(request: Request):
    form = await request.form()
    
    user_id = form["user_id"]
    risk = form["risk"]
    capital = float(form["capital"])

    advice = recommend(risk, capital)
    invoice = generate_invoice(user_id, capital)

    pie_img = allocation_pie(advice["weights"])
    hist_img = monte_carlo_histogram(advice["simulation"]["raw"])
    risk_img = risk_gauge(advice["volatility"])

    pdf_path = create_invoice_pdf(invoice)
    hist_img = monte_carlo_histogram(advice["simulation"]["raw"])
        
    return f"""
        <html>
        <head>
        <title>AI Finance Advisor — Results</title>

        <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial;
            background: #f6f8fb;
            margin: 0;
            padding: 30px;
        }}

        .container {{
            max-width: 1100px;
            margin: auto;
        }}

        h1 {{
            margin-bottom: 20px;
        }}

        .section {{
            background: white;
            padding: 25px;
            border-radius: 14px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }}


        .disclaimer {{
            background: #fff4e5;
            border-left: 6px solid #f29900;
            padding: 12px 18px;
            margin-bottom: 20px;
            border-radius: 10px;
            font-size: 14px;
            color: #663c00;
        }}


        .kpis {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }}

        .bar {{
            height: 14px;
            background: #eee;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 12px;
        }}

        .bar div {{
            height: 100%;
            background: linear-gradient(90deg, #4285f4, #34a853);
        }}

        .pct-row {{
        display: grid;
        grid-template-columns: 120px 1fr 70px;
        align-items: center;
        gap: 12px;
        margin-bottom: 14px;
    }}

    .pct-label {{
        font-weight: 600;
    }}

        
        
        .kpi {{
            padding: 20px;
            border-radius: 12px;
            background: linear-gradient(135deg, #eef3ff, #f9fbff);
        }}

        .kpi h3 {{
            margin: 0;
            font-size: 14px;
            color: #666;
        }}

        .kpi .value {{
            font-size: 28px;
            font-weight: 700;
        }}

        .green {{ color: #0f9d58; }}
        .orange {{ color: #f29900; }}
        .blue {{ color: #4285f4; }}

        .invoice {{
            background: #f8fff9;
            border: 1px dashed #b7ebc6;
        }}
        
        .pdf-btn {{
            display: inline-block;
            background: linear-gradient(135deg,#4285f4,#6fa8ff);
            color: white;
            padding: 12px 22px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            box-shadow: 0 6px 18px rgba(66,133,244,0.25);
            transition: all 0.2s ease;
        }}

        .pdf-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 22px rgba(66,133,244,0.35);
        }}

        .nav {{
            position: sticky;
            top: 12px;
            z-index: 50;

            background: white;
            padding: 14px 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-radius: 14px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.08);
            margin-bottom: 25px;
        }}

        .nav-title {{
            font-weight: 700;
            font-size: 18px;
        }}

        .nav-back {{
            text-decoration: none;
            color: #444;
            padding: 8px 14px;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-weight: 600;
        }}

        .nav-back:hover {{
            background: #f3f6fb;
        }}

        
        .nav-title {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 800;
            font-size: 18px;
        }}

        .logo-text {{
            letter-spacing: 0.3px;
        }}
        
        
        .breadcrumb {{
            font-size: 13px;
            color: #777;
            margin-bottom: 18px;
        }}
        .breadcrumb a {{
            text-decoration: none;
            color: #4285f4;
        }}

        .footer {{
            margin-top: 60px;
            padding: 22px;
            text-align: center;
            font-size: 13px;
            color: #777;
            border-top: 1px solid #eee;
        }}

        .footer a {{
            color: #4285f4;
            text-decoration: none;
            font-weight: 600;
        }}

        .alloc-card {{
            background: #ffffff;
            border-radius: 14px;
            padding: 18px;
            box-shadow: 0 6px 22px rgba(0,0,0,0.05);
            max-width: 420px;
        }}

        .alloc-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}

        .alloc-table th {{
            background: #f6f8fb;
            text-align: left;
            padding: 10px;
        }}
        
        .alloc-table td {{
            padding: 10px;
            border-bottom: 1px solid #eee;
        }}

        .alloc-table tr:last-child td {{
            border-bottom: none;
        }}

        .alloc-table td:last-child {{
            text-align: right;
            font-weight: 600;
        }}

        .alloc-grid {{
            display: grid;
            grid-template-columns: 1.3fr 1fr;
            gap: 28px;
            align-items: center;
        }}

        @media (max-width: 900px) {{
            .alloc-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        
        
        
        
        
        </style>
        </head>

        <body>
        {DISCLAIMER_HTML}
        <div class="nav">
            <div class="nav-title">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none"
                xmlns="http://www.w3.org/2000/svg">
            <path d="M3 17L9 11L13 15L21 7" stroke="#4285f4" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="9" cy="11" r="2" fill="#4285f4"/>
            <circle cx="13" cy="15" r="2" fill="#34a853"/>
            <circle cx="21" cy="7" r="2" fill="#f29900"/>
            </svg>
            <span class="logo-text">AI Finance Advisor</span>
            </div>

            <a href="/" class="nav-back">
                ← New Recommendation
            </a>
        </div>
        <div class="breadcrumb">
            <a href="/">Home</a> / <span>Recommendation</span>
        </div>
        <div class="container">

        <h1>📊 AI Portfolio Recommendation</h1>

        <div class="section">
        <h2>Key Metrics</h2>

        <div class="kpis">
            <div class="kpi">
                <h3>Expected Return</h3>
                <div class="value green">{advice["expected_return"]:.2%}</div>
            </div>

            <div class="kpi">
                <h3>Volatility</h3>
                <div class="value orange">{advice["volatility"]:.2%}</div>
            </div>

            <div class="kpi">
                <h3>Sharpe Ratio</h3>
                <div class="value blue">{advice["sharpe"]:.2f}</div>
            </div>
        </div>
        </div>

        <div class="section">

<h2>📊 Portfolio Allocation</h2>

<div class="alloc-grid">

    <div>
        <img src="data:image/png;base64,{pie_img}" width="420"/>
    </div>

    <div class="alloc-card">

        <table class="alloc-table">
        <thead>
        <tr>
            <th>Asset</th>
            <th>Weight</th>
        </tr>
        </thead>

        <tbody>
        {''.join(
            f"<tr><td>{k}</td><td>{v*100:.1f}%</td></tr>"
            for k, v in sorted(
                advice["weights"].items(),
                key=lambda x: x[1],
                reverse=True,
            )
        )}
        </tbody>

        </table>

    </div>

</div>
</div>







        <div class="section">
        <h2>Monte Carlo Outcome Distribution</h2>
        <img src="data:image/png;base64,{hist_img}" width="520"/>
        </div>

        <div class="section">
        
        <div class="section">
        <h2>📈 Monte-Carlo Outcome Percentiles</h2>

        <div class="pct-row">
        <span>Worst Case</span>
        <div class="bar">
            <div style="width:{advice["simulation"]["pct5"]/4*100:.1f}%"></div>
        </div>
        <span class="pct-label">{advice["simulation"]["pct5"]:.2f}×</span>
        </div>

        <div class="pct-row">
        <span>Median Case</span>
        <div class="bar">
            <div style="width:{advice["simulation"]["median"]/4*100:.1f}%"></div>
        </div>
        <span class="pct-label">{advice["simulation"]["median"]:.2f}×</span>
        </div>

        <div class="pct-row">
        <span>Best Case</span>
        <div class="bar">
            <div style="width:{advice["simulation"]["pct95"]/4*100:.1f}%"></div>
        </div>
        <span class="pct-label">{advice["simulation"]["pct95"]:.2f}×</span>
        </div>

        </div>



            
        <div class="section">
        <h2>🎚️ Risk Gauge</h2>
        <img src="data:image/png;base64,{risk_img}" width="520"/>
        </div>


        <div class="section invoice">
        <h2>💸 Monthly Advisory Invoice</h2>
        <ul>
        <li><b>Recommended Capital:</b> £{invoice["recommended_investment"]}</li>
        <li><b>Fee (1%):</b> £{invoice["monthly_fee"]}</li>
        <li><b>Status:</b> {invoice["status"]}</li>
        </ul>
        </div>

        <div style="margin-top:18px;">
            <a href="/download/{invoice['invoice_id']}" class="pdf-btn">
                📄 Download Invoice PDF
            </a>
         </div>
        

        </div>
                <footer class="footer">
            <div>
                <b>AI Finance Advisor</b> · v0.1.0 · Demo Build by Mohit Bhoir
            </div>

            <div>
                Data Sources: Yahoo Finance ETFs · Monte Carlo Simulation
            </div>

            <div>
                <a href="https://github.com/Mohit-Bhoir/ai-finance-advisor" target="_blank">
                    ⭐ View on GitHub
                </a>
            </div>
        </footer>

        </body>
        </html>
        """


@app.get("/download/{invoice_id}")
def download(invoice_id: str):
    return FileResponse(
        path=f"invoices/{invoice_id}.pdf",
        filename=f"invoice_{invoice_id}.pdf",
    )
