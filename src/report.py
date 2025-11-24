from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import os
from typing import Dict, Any
import logging
import pandas as pd

logger = logging.getLogger("reportgen")

def draw_histogram(df: pd.DataFrame, column: str):
    plt.figure()
    df[column].dropna().hist(bins=20)
    plt.title(f"Histogram: {column}")
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close()
    buf.seek(0)
    return buf

def write_pdf_report(stats: Dict[str, Any], df: pd.DataFrame = None, output_path: str = "/data/report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    line_y = height - 0.75 * inch

    c.setFont("Helvetica-Bold", 16)
    c.drawString(0.75 * inch, line_y, "Automated Data Summary Report")
    line_y -= 0.5 * inch

    c.setFont("Helvetica", 10)
    c.drawString(0.75 * inch, line_y, f"Rows: {stats.get('nrows')}  Columns: {stats.get('ncols')}")
    line_y -= 0.25 * inch

    c.drawString(0.75 * inch, line_y, "Missing values (per column):")
    line_y -= 0.2 * inch
    missing = stats.get("missing", {})
    for col, val in missing.items():
        c.drawString(0.9 * inch, line_y, f"{col}: {val}")
        line_y -= 0.18 * inch
        if line_y < 1.5 * inch:
            c.showPage()
            line_y = height - 0.75 * inch

    if line_y < 2 * inch:
        c.showPage()
        line_y = height - 0.75 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, line_y, "Numeric column summary:")
    line_y -= 0.25 * inch
    c.setFont("Helvetica", 10)
    numeric_stats = stats.get("numeric_stats", {})
    for col, s in numeric_stats.items():
        text = f"{col} - mean: {s['mean']}, median: {s['median']}, std: {s['std']}"
        c.drawString(0.9 * inch, line_y, text)
        line_y -= 0.18 * inch
        if line_y < 2 * inch:
            c.showPage()
            line_y = height - 0.75 * inch

    if df is not None and len(numeric_stats) > 0:
        first_col = list(numeric_stats.keys())[0]
        try:
            buf = draw_histogram(df, first_col)
            c.showPage()
            tmp_path = "/tmp/hist.png"
            with open(tmp_path, "wb") as f:
                f.write(buf.getbuffer())
            c.drawImage(tmp_path, 0.5 * inch, 2 * inch, width=7.5*inch, height=5*inch)
            try:
                os.remove(tmp_path)
            except Exception:
                pass
        except Exception as e:
            logger.warning("Failed to add histogram: %s", e)

    c.save()
