import pandas as pd


def calc_features(df_input: pd.DataFrame) -> pd.DataFrame:
    df_out = (
        df_input.groupby(["id"])
        .agg(
            count=pd.NamedAgg(column="values", aggfunc="count"),
            sum=pd.NamedAgg(column="values", aggfunc="sum"),
            max=pd.NamedAgg(column="values", aggfunc="max"),
        )
        .reset_index()
        .assign(pct_value=lambda df: round(100 * df["sum"] / sum(df["sum"]), 2))
    )
    return df_out


def calc_size(df_input: pd.DataFrame) -> int:
    return df_input.shape[0]
