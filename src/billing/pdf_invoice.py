from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path

OUTPUT_DIR = Path("invoices")
OUTPUT_DIR.mkdir(exist_ok=True)

def create_invoice_pdf(invoice: dict):
    path = OUTPUT_DIR / f"{invoice['invoice_id']}.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(str(path), pagesize=A4)
    elements = []

    elements.append(Paragraph("<b>AI Finance Advisor</b>", styles["Title"]))
    elements.append(Spacer(1, 20))

    rows = [
        ["Invoice ID", invoice["invoice_id"]],
        ["User ID", invoice["user_id"]],
        ["Recommended Capital", f"£{invoice['recommended_investment']}"],
        ["Monthly Fee", f"£{invoice['monthly_fee']}"],
        ["Status", invoice["status"]],
    ]

    table = Table(rows)
    elements.append(table)

    doc.build(elements)

    return path
