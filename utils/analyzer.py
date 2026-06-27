def get_summary_statistics(df):
    """Returns basic descriptive stats for numeric columns."""
    if df is not None and not df.empty:
        return df.describe().to_dict()
    return {}

def get_missing_values_count(df):
    """Returns a Series containing count of null values per column."""
    return df.isnull().sum()