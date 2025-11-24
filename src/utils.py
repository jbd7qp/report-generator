import csv
from statistics import mean, median

def read_csv(file_path):
    """Read CSV and return list of rows as dicts."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def summarize_data(rows):
    """Return summary stats for numeric columns, ignoring empty or invalid values."""
    if not rows:
        return {}

    summary = {}
    numeric_cols = [k for k in rows[0].keys() if all(row[k].replace('.', '', 1).isdigit() or row[k] == '' for row in rows)]

    for col in numeric_cols:
        values = []
        for row in rows:
            try:
                values.append(float(row[col]))
            except ValueError:
                pass  # skip empty or non-numeric
        if values:
            summary[col] = {
                'mean': mean(values),
                'median': median(values),
                'count': len(values)
            }
    return summary
