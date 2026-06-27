import pandas as pd
import os


def load_dataset(file_path):
    """Loads CSV, Excel, or JSON files into a pandas DataFrame."""
    if not os.path.exists(file_path):
        return None

    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV, Excel, or JSON.")


def save_processed_data(df, file_name):
    """Saves processed data to the processed folder."""
    os.makedirs("data/processed", exist_ok=True)
    out_path = os.path.join("data/processed", file_name)
    df.to_csv(out_path, index=False)
    return out_path