import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def compute_price_stats(df):
    return df["price_per_person"].median(), df["price_per_person"].mean()

def filter_small_units(df):
    return df[df["accommodates"].between(2, 4)]