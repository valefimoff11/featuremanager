import pandas as pd
import shelve

class IOInterfaces():

    def __init__(self, prices_path=None, features_path=None, db_path=None):
        self.prices_path = prices_path
        self.features_path = features_path
        self.db_path = db_path

    def get_prices_df(self):
        return pd.read_parquet(self.prices_path)
    def get_features_df(self):
        return pd.read_parquet(self.features_path)

    def persist_series_in_object_db(self, df):

        d = shelve.open(self.db_path)

        for index, value in df.items():
            d[index] = value
            print(index)

        d.close()

    def persist_df_in_object_db(self, df):

        d = shelve.open(self.db_path)

        column_names = df.columns.values.tolist()

        for column_name in column_names:
            for index in df.index.values:
                print(index)
                print(column_name + ":" + str(index))
                d[column_name + ":" + str(index)] = df.loc[index, column_name]

        d.close()

    def query_key_from_db(self, key):

        d = shelve.open(self.db_path)
        value = d[key]
        d.close()
        return value
