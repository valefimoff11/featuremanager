import pandas as pd
import numpy as np
import pyarrow.parquet as pq

def get_prices_df():
    return pd.read_parquet("E:\\tst-data\\prices.parquet")
def get_features_df():
    return pd.read_parquet("E:\\tst-data\\features.parquet")

