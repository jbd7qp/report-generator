import pandas as pd
from src.pipeline import summary_stats
import io

def test_summary_basic():
    csv = io.StringIO("""a,b,c
1,2,3
4,5,6
7,,9
""")
    df = pd.read_csv(csv)
    stats = summary_stats(df)
    assert stats['nrows'] == 3
    assert 'b' in stats['missing']
    assert stats['numeric_stats']['a']['mean'] == 4.0
