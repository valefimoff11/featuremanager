from src.datamanagement.data_manager import df_shift

def test_shift(dummy_df):

    shifted_df = df_shift(dummy_df, target="c1", lag=1)

    assert shifted_df.loc[1, "c2"] == 1
    assert shifted_df.loc[1, "c3"] == 1