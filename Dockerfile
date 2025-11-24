FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    libssl-dev \
    libpng-dev \
    libjpeg-dev \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY run.sh .
COPY assets/ assets/

ENV PYTHONUNBUFFERED=1

ENV INPUT_CSV=/data/sample.csv
ENV OUTPUT_PDF=/data/report.pdf
ENV LOG_LEVEL=INFO
ENV METRICS_PATH=/data/metrics.json

VOLUME ["/data"]

ENTRYPOINT ["/bin/bash", "/app/run.sh"]
