import pandas as pd






def deduplicate_customers(df: pd.DataFrame) -> pd.DataFrame:


    df = df.copy()


    df = df.sort_values(
        by=["customer_id","email"],
        kind="stable"
    )



    df = df.drop_duplicates(
        subset=["customer_id"],
        keep="first"

    )


    df = df.reset_index(drop=True)


    return df


