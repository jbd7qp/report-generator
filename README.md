# Report Generator API – Case Study

---

## 1) Executive Summary

### Problem  
Users often work with CSV files and need a simple way to compute summary statistics and generate a clean PDF report without installing analytics software. The problem is to create a lightweight, containerized microservice that reads a dataset, summarizes it, and outputs a report.

### Solution  
This project provides a Flask-based API that accepts a CSV file, computes summary statistics, and generates a downloadable PDF report. The system runs fully inside a Docker container and can also be deployed to Azure App Service. The application produces numeric summaries for each numeric column and stores generated PDFs in a `reports/` directory.

---

## 2) System Overview

### Course Concept(s)  
Containerization (Docker), REST APIs, Microservice Patterns, Data Processing Pipelines, Report Generation, Cloud Deployment (optional).

### Architecture Diagram  
See `/assets/architecture.png` (embedded below):

![Architecture Diagram](assets/architecture.png)

### Data / Models / Services

**Data Source:** `assets/sample.csv`  
**Format:** CSV (~10 rows, numeric & categorical fields)  
**License:** Created for class assignment; no external licensing required  

**Services Used:**  
- Flask web service  
- ReportLab PDF generator  
- Docker container runtime  
- Optional Azure App Service deployment  

---

## 3) How to Run (Local)

### Docker

```bash
# build
docker build -t report-api .

# run (bind reports folder so PDFs save locally)
docker run -p 8080:8080 -v $(pwd)/reports:/app/reports report-api

# health test
curl http://localhost:8080/

# generate report
curl -O -J "http://localhost:8080/generate?file=assets/sample.csv"

A PDF will be created in the local reports/ directory with a timestamped filename such as:
report_20251126_192225.pdf

---

## 4) Design Decisions

Why this concept?
Docker was chosen to ensure reproducibility and eliminate environment setup issues. Flask provides a minimal, fast API layer for CSV input and PDF output. ReportLab allows deterministic, low-dependency PDF generation.

Alternatives Considered
FastAPI (more features but unnecessary for a single endpoint)
Pandas (heavier dependency; custom code was enough for summary stats)
Cloud storage for reports (not required for this assignment)

Tradeoffs
Simplicity vs. flexibility: Hard-coded PDF layout for reliability
Lightweight implementation but not intended for large datasets
Minimal API (single-purpose microservice)

Security / Privacy
No PII data processed
No secrets required
Input CSV validated by checking file existence
No environment variables needed for local or cloud execution

Ops
Logging to stdout (compatible with Azure App Service)
Scaling: Stateless container; replicas could run independently
Known Limitations:
No CSV upload—file must exist on server
No large dataset optimizations
Cloud deployment does not allow file uploads (GET-based demo only)

---

## 5) Results & Evaluation

Screenshots and Outputs (stored in /assets)
assets/report_screenshot.png – Screenshot of generated PDF download
assets/architecture.png – Architecture diagram

Sample generated PDF included:
reports/report_20251126_192225.pdf

Behavior
Summarizes numeric columns (id, value_a, value_b)
Skips non-numeric columns such as category
Generates a clean PDF formatted with ReportLab

Validation / Tests
Local test of /generate endpoint using sample CSV
Verified PDF output stored into mounted reports directory
Confirmed container runs consistently through multiple rebuilds

Performance Notes
Complexity is O(n) for CSV scan
PDF generation < 0.01s for small datasets
Container size stays minimal due to few dependencies

---

## 6) What’s Next

- Add CSV upload via POST
- Expand PDF layout (tables, charts, branding)
- Add unit tests for summary logic
- Add FastAPI version for better docs and validation
- Add authentication or API keys for multi-user deployments

---

## 7) Links

GitHub Repo:
https://github.com/jbd7qp/report-generator

Public Cloud App:
https://reportgen-app-d9c781.azurewebsites.net/
