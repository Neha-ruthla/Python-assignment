import pandas as pd

def load_data(path):
    """Load CSV file"""
    return pd.read_csv(path)

def save_data(df, path):
    """Save CSV file to output folder"""
    df.to_csv(path, index=False)
