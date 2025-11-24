import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from utils import read_csv, summarize_data  # absolute import

def generate_pdf(summary, output_path="report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750
    c.drawString(50, y, "CSV Summary Report")
    y -= 40
    for col, stats in summary.items():
        c.drawString(50, y, f"{col}: Mean={stats['mean']:.2f}, Median={stats['median']:.2f}, Count={stats['count']}")
        y -= 20
    c.save()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 src/main.py <csv_file>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    rows = read_csv(csv_file)
    summary = summarize_data(rows)
    generate_pdf(summary)
    print(f"Report generated: report.pdf")

if __name__ == "__main__":
    main()
