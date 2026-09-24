import pandas as pd


def normalize_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize raw customer data into our canonical format.
    """

    # Make a copy so we don't modify the original raw data
    df = df.copy()

    text_columns = [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "zip",
        "balance"
    ]

    # Remove extra spaces
    for column in text_columns:
        df[column] = df[column].str.strip()

    # Standardize names
    df["first_name"] = df["first_name"].str.title()
    df["last_name"] = df["last_name"].str.title()

    # Standardize email
    df["email"] = df["email"].str.lower()

    return df