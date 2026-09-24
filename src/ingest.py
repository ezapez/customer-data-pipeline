from pathlib import Path
import pandas as pd



def load_partner_file(file_path):
    df = pd.read_csv(

        file_path,
        dtype=str
    )

    return df 




if __name__== "__main__":
    file_path = Path("data/incoming/partner_a.csv")
    customers = load_partner_file(file_path)

    print(customers)

    print("\nCOLUMN TYPES")
    print(customers.dtypes)
