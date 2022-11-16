import pandas as pd
import os
import pytest

@pytest.fixture
def get_df(filename = "Data/demo_AmexTransactions.csv"):
    df1 = pd.read_csv(f"{filename}", header=None)
    print(df1)
    return df1

def test_count_records(get_df):
    df1 = get_df
    import_count = len(df1.index)
    print(f"\nimport_count: {import_count}\n")
    assert import_count == 8
