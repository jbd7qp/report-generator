# Report Generator API

This project provides a containerized Flask API that reads a CSV file, computes summary statistics, and produces a PDF report. It supports both local execution using Docker and an optional cloud deployment on Azure App Service.

---

## Features

- Reads CSV files and computes mean, median, and count for numeric columns  
- Generates a PDF report using ReportLab  
- Exposes a REST API endpoint for generating reports  
- Containerized using Docker  
- Automatically saves generated PDFs into a local `reports/` directory  
- Optional cloud deployment using Azure App Service  

---

## Repository Structure

```
report-generator/
│
├── assets/
│   ├── sample.csv
│   ├── architecture.png
│   └── report_screenshot.png
│
├── reports/               # Created at runtime, stores generated PDFs
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── main.py
│   ├── utils.py
│   └── report.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── run.sh
```

---

## Architecture Diagram

The system architecture is shown below:

![Architecture](assets/architecture.png)

---

## How to Run Locally

### 1. Build the Docker image
```bash
docker build -t report-api .
```

### 2. Run the container
```bash
docker run -p 8080:8080 -v $(pwd)/reports:/app/reports report-api
```

This mounts the local `reports/` directory so generated PDFs are saved to your machine.

---

## Generating a Report

In a separate terminal:

```bash
curl -O -J "http://localhost:8080/generate?file=assets/sample.csv"
```

A PDF will appear in the `reports/` folder with a name like:

```
report_20251126_192225.pdf
```

---

## Cloud Deployment

This application is deployed on Azure App Service:

**Base URL:**  
https://reportgen-app-d9c781.azurewebsites.net/

**Generate PDF report:**  
https://reportgen-app-d9c781.azurewebsites.net/generate

The cloud deployment uses the embedded sample CSV.

---

## Results and Evaluation

### Example Generated Report  
The sample PDF is located here:

```
assets/report_20251126_192225.pdf
```

### Screenshot of Output  
Included here:

```
assets/report_screenshot.png
```

---

## Sample Output Preview

The generated PDF summarizes each numeric column in the CSV:

- Mean  
- Median  
- Count  

`sample.csv` includes columns such as:

- id  
- value_a  
- value_b  
- category (ignored as non-numeric)

---

## Environment Variables

This project **does not use a `.env` file**.  
No secrets or environment variables are required for local or cloud execution.

---

## Requirements

Python dependencies (listed in `requirements.txt`):

- Flask  
- ReportLab  

---

## Contact

For questions or issues, contact the developer.
