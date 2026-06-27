import pandas as pd


def clean_data(df, fill_method="mean", drop_duplicates=True):
    """Cleans the DataFrame by removing duplicates and imputing missing values."""
    cleaned_df = df.copy()

    if drop_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()

    numeric_cols = cleaned_df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        if fill_method == "mean":
            cleaned_df[col].fillna(cleaned_df[col].mean(), inplace=True)
        elif fill_method == "median":
            cleaned_df[col].fillna(cleaned_df[col].median(), inplace=True)
        elif fill_method == "zero":
            cleaned_df[col].fillna(0, inplace=True)

    non_numeric_cols = cleaned_df.select_dtypes(exclude=['number']).columns
    for col in non_numeric_cols:
        cleaned_df[col].fillna("Unknown", inplace=True)

    return cleaned_df