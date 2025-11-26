import logging
import sys
import os
from datetime import datetime

from flask import Flask, send_file, request, jsonify

from src.utils import read_csv, summarize_data
from src.main import generate_pdf

# Configure logging for stdout (Azure App Service compatible)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

app = Flask(__name__)

# Ensure reports directory exists
REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

@app.route("/")
def home():
    logging.info("Home endpoint hit.")
    return jsonify({"message": "Report Generator API is running."})

@app.route("/generate", methods=["GET"])
def generate():
    logging.info("Generate endpoint called.")

    csv_file = request.args.get("file", "assets/sample.csv")
    logging.info(f"Requested CSV file: {csv_file}")

    if not os.path.exists(csv_file):
        logging.error(f"CSV file not found: {csv_file}")
        return jsonify({"error": f"CSV file not found: {csv_file}"}), 400

    try:
        rows = read_csv(csv_file)
        logging.info(f"Read {len(rows)} rows from CSV.")

        summary = summarize_data(rows)
        logging.info("Summary generated.")

        # Unique filename using timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(REPORTS_DIR, f"report_{timestamp}.pdf")

        generate_pdf(summary, output_path)
        logging.info(f"PDF generated: {output_path}")

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        logging.exception("Error during /generate request.")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logging.info(f"Starting Flask app on port {port}")
    app.run(host="0.0.0.0", port=port)
