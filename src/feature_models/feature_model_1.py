import sys

import pandas as pd

from src.datamanagement.data_manager import df_shift
from src.featurereader.rd import get_prices_df, get_features_df

time_lags = [1, 5, 10]
number_of_timelags = len(time_lags)
cors = {}

prices_df = get_prices_df()
features_df = get_features_df()

print(prices_df)
print(features_df)

feature_names = features_df.columns.values.tolist()
feature_names.remove('timestamp')

for feature_name in feature_names:
    cors.update({feature_name: number_of_timelags * [None]})

feature_price_cor_df = pd.DataFrame(cors, index=time_lags)
print(feature_price_cor_df)
#feature_price_cor_df.loc[1, 'feature_0'] =0.9
#print(feature_price_cor_df)

model_dataset_df = pd.concat([prices_df["price"], features_df], axis=1)
print(model_dataset_df)

for lag in time_lags:
    model_df_shifted = df_shift(model_dataset_df, 'price', lag=-1*lag)
    print(model_df_shifted)
    print(model_df_shifted['feature_0'].corr(model_df_shifted['price']))

sys.exit()

print( df_new['feature_0'].corr(df_new['feature_1']) )
print()
print(features_df)
print()
print(df_new)
print()
print(df_new.corr())


print()
print(model_dataset_df)

