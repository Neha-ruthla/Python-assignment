import pandas as pd

def clean_data(df):
    """Clean and preprocess weather data"""
    
    # Remove rows with all empty values
    df = df.dropna(how='all')

    # Fill missing numeric values with mean
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Convert date column to datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows where date could not be converted
    df = df.dropna(subset=['date'])

    print("Data cleaned successfully!")
    return df
