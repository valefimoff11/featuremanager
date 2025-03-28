import sys
import pandas as pd

from src.datamanagement.data_manager import df_shift
from src.io_interfaces.io_interfaces import IOInterfaces


class FeatureStatsModel():

    def __init__(self, io_interfaces=None):
        self.io_interfaces = io_interfaces

    def set_io_interfaces(self, io_interfaces):
        self.io_interfaces = io_interfaces

    def run_model(self):

        # for prod solution the list of timelags would be populated from config file
        time_lags = [1, 5, 10]
        number_of_timelags = len(time_lags)
        cors = {}

        #################################################################################################################
        #
        # Data Preparation: Input Data
        #
        #################################################################################################################

        prices_df = self.io_interfaces.get_prices_df()
        features_df = self.io_interfaces.get_features_df()

        print(prices_df)
        print(features_df)

        feature_names = features_df.columns.values.tolist()
        feature_names.remove('timestamp')

        for feature_name in feature_names:
            cors.update({feature_name: number_of_timelags * [None]})

        feature_price_cor_df = pd.DataFrame(cors, index=time_lags)
        print(feature_price_cor_df)

        model_dataset_df = pd.concat([prices_df["price"], features_df], axis=1)
        print(model_dataset_df)


        #################################################################################################################
        #
        # Calculation of Price Returns
        #
        #################################################################################################################
        model_dataset_df['price_return'] = model_dataset_df['price'].pct_change(1)

        model_dataset_df = model_dataset_df.dropna()
        print(model_dataset_df)

        #################################################################################################################
        #
        # Calculation of Correlation of Features to Price Returns at range of timelags
        #
        #################################################################################################################
        for lag in time_lags:
            model_df_shifted = df_shift(model_dataset_df, 'price_return', lag=-1*lag)
            model_df_shifted = model_df_shifted.dropna()
            print(model_df_shifted)
            for feature_name in feature_names:
                feature_price_cor_df.loc[lag, feature_name] = model_df_shifted[feature_name].corr(model_df_shifted['price_return'])
                print(model_df_shifted[feature_name].corr(model_df_shifted['price_return']))

        print()
        print(feature_price_cor_df)
        print(type(feature_price_cor_df))

        #################################################################################################################
        #
        # Calculation of Correlation Matrix of Features
        #
        #################################################################################################################
        print()
        features_only_df = features_df[features_df.columns.difference(['timestamp'])]
        features_correlation_matrix = features_only_df.corr()
        print(features_correlation_matrix)
        print(type(features_correlation_matrix))

        #################################################################################################################
        #
        # Calculation of Standard Deviation of Features
        #
        #################################################################################################################
        print()
        features_std = features_only_df.std()
        print(features_std)

        #################################################################################################################
        #
        # Data Preparation: Persist Output Data to simulated external, key/value DB
        #
        #################################################################################################################

        self.io_interfaces.persist_df_in_object_db(feature_price_cor_df)
        self.io_interfaces.persist_df_in_object_db(features_correlation_matrix)
        self.io_interfaces.persist_series_in_object_db(features_std)


if __name__ == '__main__':

    DB_LOCATION = "E:\\tst-data\\feature_stats_db"
    FEATURES_PATH = "E:\\tst-data\\features.parquet"
    PRICES_PATH = "E:\\tst-data\\prices.parquet"

    io_interfcaes = IOInterfaces(PRICES_PATH, FEATURES_PATH, DB_LOCATION)

    FeatureStatsModel(io_interfcaes).run_model()