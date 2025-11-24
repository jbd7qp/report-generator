import pandas as pd
import numpy as np
from typing import Dict, Any
import logging

def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def summary_stats(df: pd.DataFrame) -> Dict[str, Any]:
    numeric = df.select_dtypes(include=[np.number])
    stats = {}
    stats['nrows'] = int(len(df))
    stats['ncols'] = int(df.shape[1])
    stats['missing'] = df.isnull().sum().to_dict()
    stats['numeric_stats'] = {}
    for col in numeric.columns:
        s = numeric[col].dropna()
        stats['numeric_stats'][col] = {
            'mean': float(s.mean()) if len(s) > 0 else None,
            'median': float(s.median()) if len(s) > 0 else None,
            'std': float(s.std(ddof=0)) if len(s) > 0 else None,
            'min': float(s.min()) if len(s) > 0 else None,
            'max': float(s.max()) if len(s) > 0 else None,
            'count': int(s.count())
        }
    return stats
