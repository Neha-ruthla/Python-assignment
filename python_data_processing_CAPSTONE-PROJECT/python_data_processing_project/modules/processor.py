def clean_data(df):
    """Clean data: remove null, duplicates"""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def calculate_summary(df, column):
    """Return basic statistics of a given column"""
    return {
        "min": df[column].min(),
        "max": df[column].max(),
        "mean": df[column].mean(),
        "sum": df[column].sum()
    }
