#!/usr/bin/env bash
set -euo pipefail

INPUT=${INPUT_CSV:-/data/sample.csv}
OUTPUT=${OUTPUT_PDF:-/data/report.pdf}
LOG_LEVEL=${LOG_LEVEL:-INFO}

mkdir -p "$(dirname "$OUTPUT")"
mkdir -p /app/logs

python3 -m src.main --input "$INPUT" --output "$OUTPUT" --log-level "$LOG_LEVEL"

echo "Report generated at: $OUTPUT"
