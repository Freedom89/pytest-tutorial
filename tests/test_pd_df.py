import pandas as pd
import pytest
from src.pd_df import calc_features, calc_size


@pytest.fixture
def mock_dataframe():
    df_dummy = pd.DataFrame(
        dict(id=[1, 1, 2, 2, 3, 3, 3], values=[3, 5, 6, 7, 8, 9, 15])
    )
    return df_dummy


@pytest.fixture
def mock_results():
    df_check = pd.DataFrame(
        {
            "id": {0: 1, 1: 2, 2: 3},
            "count": {0: 2, 1: 2, 2: 3},
            "sum": {0: 8, 1: 13, 2: 32},
            "max": {0: 5, 1: 7, 2: 15},
            "pct_value": {0: 15.09, 1: 24.53, 2: 60.38},
        }
    )
    return df_check


def test_calc_features(mock_dataframe, mock_results):
    pd.testing.assert_frame_equal(
        calc_features(mock_dataframe), mock_results
    ), "something went wrong"


def test_calc_size(mock_dataframe):
    assert calc_size(mock_dataframe) == 7, "something went wrong"

