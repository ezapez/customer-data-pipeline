CREATE TABLE IF NOT EXISTS customer_history (
    customer_sk BIGSERIAL PRIMARY KEY,

    customer_id varchar(50) NOT NUll,

    first_name varchar(50),
    last_name varchar(50),
    email varchar(100),
    zip varchar(20),

    balance numeric(12,2),

    effective_from TIMESTAMP NOT NULL,
    effective_to TIMESTAMP,


    is_current BOOLEAN NOT NULL DEFAULT TRUE

    check(
        effective_to > effective_from
    )
);


CREATE UNIQUE INDEX IF NOT EXISTS one_current_record_per_customer
ON customer_history (customer_id)
WHERE is_current = TRUE;

