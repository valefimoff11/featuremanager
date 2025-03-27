import pandas as pd
import shelve

DB_LOCATION = "E:\\tst-data\\feature_stats_db"

def get_prices_df():
    return pd.read_parquet("E:\\tst-data\\prices.parquet")
def get_features_df():
    return pd.read_parquet("E:\\tst-data\\features.parquet")

def persist_series_in_object_db(df):

    d = shelve.open(DB_LOCATION)

    for index, value in df.items():
        d[index] = value
        print(index)

    d.close()

def persist_df_in_object_db(df):

    d = shelve.open(DB_LOCATION)

    column_names = df.columns.values.tolist()

    for column_name in column_names:
        for index in df.index.values:
            print(index)
            print(column_name + ":" + str(index))
            d[column_name + ":" + str(index)] = df.loc[index, column_name]

    d.close()

def query_key_from_db(key):

    d = shelve.open(DB_LOCATION)
    value = d[key]
    d.close()
    return value
