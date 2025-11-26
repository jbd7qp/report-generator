Report Generator API

This project provides a containerized Flask API that reads a CSV file, generates summary statistics, and produces a PDF report. It supports local execution using Docker and includes a deployed cloud version on Azure App Service.

Features

Reads CSV files and computes mean, median, and count for numeric columns

Generates a PDF report using ReportLab

Exposes a REST API endpoint for generating reports

Containerized using Docker

Automatically saves generated PDFs into a reports directory

Optional cloud deployment using Azure App Service

Repository Structure
report-generator/
│
├── assets/
│   ├── sample.csv
│   ├── architecture.png
│   └── report_screenshot.png
│
├── reports/                (created at runtime, stores generated PDFs)
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

Architecture Diagram

The system architecture is shown in the image below:

assets/architecture.png

How to Run Locally
1. Build the Docker image
docker build -t report-api .

2. Run the container
docker run -p 8080:8080 -v $(pwd)/reports:/app/reports report-api


This mounts the local reports directory so you can access generated PDFs on your machine.

3. Generate a report

In a separate terminal run:

curl -O -J "http://localhost:8080/generate?file=assets/sample.csv"


A new PDF file will be created inside the reports folder with a name like:

report_20251126_192225.pdf

Cloud Deployment

This application is deployed on Azure App Service at the following URL:

https://reportgen-app-d9c781.azurewebsites.net/


Home endpoint:

https://reportgen-app-d9c781.azurewebsites.net/


Generate PDF report (uses the embedded sample CSV):

https://reportgen-app-d9c781.azurewebsites.net/generate

Results and Evaluation
Example Generated Report

A sample generated PDF is included in the repository:

assets/report_20251126_192225.pdf

Screenshot of the Output

A screenshot of the downloaded PDF from the browser is included:

assets/report_screenshot.png

Sample Output Preview

The PDF summarizes each numeric column in the CSV:

Mean

Median

Count

Example rows from sample.csv include:

id

value_a

value_b

category

The API correctly excludes non-numeric columns such as category.

Environment Variables

This project does not use a .env file. No secrets or environment variables are required for local or cloud execution.

Requirements

Python libraries used:

Flask

ReportLab

All dependencies are listed in requirements.txt.

Contact

For any questions or issues, contact the developer.
