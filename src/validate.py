from decimal import Decimal, InvalidOperation
import pandas as pd

def is_valid_email(email: str) -> bool:
    if not email:
        return False

    return "@"  in email and "." in email.split("@")[-1]

def is_valid_balance(balance: str) -> bool:
    try:
        Decimal(balance)
        return True
    except(InvalidOperation, TypeError, ValueError):
        return False
def validate_customers(df: pd.DataFrame):
    valid_rows = []
    invalid_rows = []


    for _, row in df.iterrows():
        reasons = []
        if not row["customer_id"]:
            reasons.append("missing customer_id")

        if not is_valid_email(row["email"]):
            reasons.append("Invalid email")

        if not is_valid_balance(row["balance"]):
            reasons.append("invalid balance")

        if reasons:
            bad_row = row.copy()
            bad_row["quarantine_reason"] = ";".join(reasons)
            invalid_rows.append(bad_row)
        else:
            valid_rows.append(row)

    valid_df = pd.DataFrame(valid_rows)
    invalid_df = pd.DataFrame(invalid_rows)

    return valid_df, invalid_df







