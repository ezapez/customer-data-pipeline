from pathlib import Path 



from ingest import load_partner_file
from normalize import normalize_customers
from  validate import validate_customers
from deduplicate import deduplicate_customers



PROJECT_ROOT = Path(__file__).resolve().parent.parent


INPUT_FILE = PROJECT_ROOT / "data" / "incoming" / "partner_a.csv" # data -> incoming -> partner_a.csv
QUARANTINE_FILE = (
    PROJECT_ROOT / "data" / "quarantine" / "rejected_rows.csv"
)  # data -> quarantine -> rejected_rows.csv





def main():
    print("Starting customer data pipeline...")


    # loadind raw customer data pipeline
    raw = load_partner_file(INPUT_FILE)
    print(f"Loaded {len(raw)} rows")


    # normalized the date

    normalized = normalize_customers(raw)
    print("Normalization complete")



    # Validate the data 

    valid, invalid = validate_customers(normalized)

    print(f"Valid rows: {len(valid)}")
    print(f"Invalid rows: {len(invalid)}")


    if not invalid.empty:
        invalid.to_csv(
            QUARANTINE_FILE,
            index=False
        )

        print(f"Rejected rows saved to: {QUARANTINE_FILE}")

    deduplicated = deduplicate_customers(valid)

    print(f"Rows before  deduplication: {len(valid)}")
    print(f"Rows after deduplication: {len(deduplicated)}")


    print("\nDeduplicated customers:")
    print(deduplicated)

    print("Pipeline complete.")






if __name__ == "__main__":
    main()






