import pandas as pd
import pytest

@pytest.fixture
def dummy_df():
    return pd.DataFrame({"c1": [1,2,3], "c2": [1,2,3], "c3": [1,2,3]})