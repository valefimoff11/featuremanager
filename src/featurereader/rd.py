import pandas as pd
import numpy as np
import pyarrow.parquet as pq

prices_df = pd.read_parquet("E:\\tst-data\\prices.parquet")

features_df = pd.read_parquet("E:\\tst-data\\features.parquet")

print(prices_df)
print()
print(features_df)