CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id TEXT,
    amfi_code INTEGER,
    date_id INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    date_id INTEGER,
    aum REAL,
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);