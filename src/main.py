import argparse
import os
import json
from .pipeline import load_csv, summary_stats
from .report import write_pdf_report
from .utils import setup_logger
import logging
import time
import pandas as pd

logger = logging.getLogger("reportgen")

def run(input_csv: str, output_pdf: str, log_level: str = "INFO"):
    logger = setup_logger(log_level)
    t0 = time.time()
    logger.info("Loading CSV: %s", input_csv)
    if not os.path.exists(input_csv):
        logger.error("Input CSV not found: %s", input_csv)
        raise FileNotFoundError(input_csv)
    df = load_csv(input_csv)
    stats = summary_stats(df)
    logger.info("Computed stats: rows=%s cols=%s", stats['nrows'], stats['ncols'])
    logger.info("Generating PDF report to: %s", output_pdf)
    write_pdf_report(stats, df=df, output_path=output_pdf)
    duration = time.time() - t0
    metrics = {
        "rows": stats['nrows'],
        "cols": stats['ncols'],
        "duration_seconds": duration
    }
    metrics_path = os.environ.get("METRICS_PATH", "/data/metrics.json")
    try:
        with open(metrics_path, "w") as fh:
            json.dump(metrics, fh)
        logger.info("Metrics written to %s", metrics_path)
    except Exception as e:
        logger.warning("Failed to write metrics: %s", e)
    logger.info("Finished. Duration: %.2fs", duration)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PDF report from CSV")
    parser.add_argument("--input", "-i", required=True, help="Path to input CSV")
    parser.add_argument("--output", "-o", required=True, help="Path to output PDF")
    parser.add_argument("--log-level", default="INFO", help="Log level")
    args = parser.parse_args()
    run(args.input, args.output, args.log_level)
