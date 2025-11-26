import csv

def read_csv(file_path):
    """Read CSV file and return a list of dict rows."""
    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def summarize_data(rows):
    """Summarize numeric columns: mean, median, count."""
    if not rows:
        return {}
    
    summary = {}
    for col in rows[0].keys():
        numeric_data = []
        for row in rows:
            try:
                val = float(row[col])
                numeric_data.append(val)
            except (ValueError, TypeError):
                continue  # skip non-numeric or missing
        
        if numeric_data:
            numeric_data.sort()
            n = len(numeric_data)
            median = numeric_data[n // 2] if n % 2 == 1 else (numeric_data[n//2 - 1] + numeric_data[n//2]) / 2
            summary[col] = {
                "mean": sum(numeric_data) / n,
                "median": median,
                "count": n
            }
    return summary
