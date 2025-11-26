FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY assets/ assets/

ENV PYTHONPATH=/app

EXPOSE 8080

# Use Gunicorn to run Flask app inside src package
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "src.app:app", "--workers", "1"]
