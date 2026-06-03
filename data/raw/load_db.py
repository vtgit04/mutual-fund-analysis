import pandas as pd
from sqlalchemy import create_engine

# Create database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load CSVs
fund = pd.read_csv("01_fund_master.csv")
nav = pd.read_csv("nav_history_clean.csv")
txn = pd.read_csv("investor_transactions_clean.csv")
perf = pd.read_csv("scheme_performance_clean.csv")
aum = pd.read_csv("03_aum_by_fund_house.csv")
sip = pd.read_csv("../processed/monthly_sip_inflows_clean.csv")
category = pd.read_csv("../processed/category_inflows_clean.csv")
folio = pd.read_csv("../processed/industry_folio_count_clean.csv")
portfolio = pd.read_csv("../processed/portfolio_holdings_clean.csv")
benchmark = pd.read_csv("../processed/benchmark_indices_clean.csv")

# Load into SQLite
fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

sip.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

category.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)

folio.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

portfolio.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

benchmark.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully!")