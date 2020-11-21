import pandas as pd

df_dummy = pd.DataFrame(dict(id=[1, 1, 2, 2, 3, 3, 3], values=[3, 5, 6, 7, 8, 9, 15]))

df_stats = (
    df_dummy.groupby(["id"])
    .agg(
        count=pd.NamedAgg(column="values", aggfunc="count"),
        sum=pd.NamedAgg(column="values", aggfunc="sum"),
        max=pd.NamedAgg(column="values", aggfunc="max"),
    )
    .reset_index()
    .assign(pct_value=lambda df: round(100 * df["sum"] / sum(df["sum"]), 2))
)

# To double check - you might sample a column

df_temp = df_dummy.loc[lambda x: x["id"] == 1][["values"]]
df_temp.sum().values
df_temp.max().values

# Or you would do this:

df_check = pd.DataFrame(
    {
        "id": {0: 1, 1: 2, 2: 3},
        "count": {0: 2, 1: 2, 2: 3},
        "sum": {0: 8, 1: 13, 2: 32},
        "max": {0: 5, 1: 7, 2: 15},
        "pct_value": {0: 15.09, 1: 24.53, 2: 60.38},
    }
)

pd.testing.assert_frame_equal(df_stats, df_check)

