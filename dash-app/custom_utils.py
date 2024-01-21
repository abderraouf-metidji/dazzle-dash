import pandas as pd

def round_numeric_columns(df, precision=2):
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = df[numeric_columns].round(precision)
    return df
