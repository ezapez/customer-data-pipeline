import pandas as pd

from src.deduplicate import deduplicate_customers


def test_removes_duplicate_customers():
    data = {
        "customer_id" :["1001", "1002", "1002", "1003"],
        "first_name": ["John","Mary","Mary","Bob"],
        "email" : [
            "john@email.com",
            "mary@email.com",
            "mary@email.com",
            "bob@email.com"
        ]
    }


    df = pd.DataFrame(data)

    result = deduplicate_customers(df)

    assert len(result) == 3

    assert result["customer_id"].tolist() == [
        "1001",
        "1002",
        "1003"
    ]


    
