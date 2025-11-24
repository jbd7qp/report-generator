import sys
import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from utils import read_csv, summarize_data

# Configure logging
logging.basicConfig(
    filename="report_generator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_pdf(summary, output_path="report.pdf"):
    """Generate a simple PDF report from summary stats."""
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750
    c.drawString(50, y, "CSV Summary Report")
    y -= 40
    for col, stats in summary.items():
        c.drawString(50, y, f"{col}: Mean={stats['mean']:.2f}, Median={stats['median']:.2f}, Count={stats['count']}")
        y -= 20
    c.save()
    logging.info(f"PDF report generated at {output_path}")

def main():
    if len(sys.argv) < 2:
        logging.error("CSV file not provided")
        print("Usage: python3 src/main.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    try:
        rows = read_csv(csv_file)
        summary = summarize_data(rows)
        generate_pdf(summary)
        logging.info(f"Processed CSV file: {csv_file}")
        print(f"Report generated: report.pdf")
    except FileNotFoundError:
        logging.error(f"File not found: {csv_file}")
        print(f"Error: File not found - {csv_file}")
    except Exception as e:
        logging.exception("Unexpected error")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
