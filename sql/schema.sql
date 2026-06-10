-- Bluestock Fintech — Mutual Fund Analysis
-- SQLite Star Schema

-- Dimension: Fund Master
CREATE TABLE IF NOT EXISTS fund_master (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT
);

-- Dimension: Benchmark Indices
CREATE TABLE IF NOT EXISTS benchmark_indices (
    date TEXT,
    index_name TEXT,
    close_value REAL
);

-- Fact: NAV History
CREATE TABLE IF NOT EXISTS nav_history (
    amfi_code INTEGER,
    date TEXT,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);

-- Fact: Investor Transactions
CREATE TABLE IF NOT EXISTS investor_transactions (
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);

-- Fact: Scheme Performance
CREATE TABLE IF NOT EXISTS scheme_performance (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    alpha REAL,
    beta REAL,
    expense_ratio_pct REAL,
    risk_grade TEXT,
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);

-- Dimension: AUM by Fund House
CREATE TABLE IF NOT EXISTS aum_by_fund_house (
    date TEXT,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER
);

-- Dimension: Monthly SIP Inflows
CREATE TABLE IF NOT EXISTS monthly_sip_inflows (
    month TEXT PRIMARY KEY,
    sip_inflow_crore REAL,
    active_sip_accounts_crore REAL,
    new_sip_accounts_lakh REAL,
    sip_aum_lakh_crore REAL
);

-- Dimension: Category Inflows
CREATE TABLE IF NOT EXISTS category_inflows (
    month TEXT,
    category TEXT,
    net_inflow_crore REAL
);

-- Dimension: Industry Folio Count
CREATE TABLE IF NOT EXISTS industry_folio_count (
    month TEXT PRIMARY KEY,
    total_folios_crore REAL,
    equity_folios_crore REAL,
    debt_folios_crore REAL,
    hybrid_folios_crore REAL
);

-- Dimension: Portfolio Holdings
CREATE TABLE IF NOT EXISTS portfolio_holdings (
    amfi_code INTEGER,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL,
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);
