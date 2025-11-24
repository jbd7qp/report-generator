import pandas as pd
import os
from src.report import write_pdf_report
from src.pipeline import summary_stats

def test_report_creates_pdf(tmp_path):
    df = pd.DataFrame({"x":[1,2,3], "y":[4,5,6]})
    stats = summary_stats(df)
    out = tmp_path / "out.pdf"
    write_pdf_report(stats, df=df, output_path=str(out))
    assert out.exists()
    assert out.stat().st_size > 1000
