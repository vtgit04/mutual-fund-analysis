# Data Dictionary

# Source Files

## 01_fund_master.csv

| Column       | Data Type | Description                   |
| ------------ | --------- | ----------------------------- |
| amfi_code    | INTEGER   | Unique AMFI scheme identifier |
| scheme_name  | TEXT      | Mutual fund scheme name       |
| fund_house   | TEXT      | Asset Management Company      |
| category     | TEXT      | Fund category                 |
| sub_category | TEXT      | Fund sub-category             |

---

## 02_nav_history.csv

| Column    | Data Type | Description            |
| --------- | --------- | ---------------------- |
| amfi_code | INTEGER   | AMFI scheme identifier |
| date      | DATE      | NAV reporting date     |
| nav       | REAL      | Net Asset Value        |

---

## 03_aum_by_fund_house.csv

| Column         | Data Type | Description                          |
| -------------- | --------- | ------------------------------------ |
| date           | DATE      | Reporting date                       |
| fund_house     | TEXT      | Asset Management Company             |
| aum_lakh_crore | REAL      | Assets Under Management (Lakh Crore) |
| aum_crore      | REAL      | Assets Under Management (Crore)      |
| num_schemes    | INTEGER   | Number of schemes managed            |

---

## 04_monthly_sip_inflows.csv

| Column     | Data Type | Description               |
| ---------- | --------- | ------------------------- |
| month      | DATE/TEXT | Reporting month           |
| sip_inflow | REAL      | Monthly SIP inflow amount |

---

## 05_category_inflows.csv

| Column   | Data Type | Description          |
| -------- | --------- | -------------------- |
| category | TEXT      | Mutual fund category |
| inflow   | REAL      | Net inflow amount    |

---

## 06_industry_folio_count.csv

| Column      | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| category    | TEXT      | Fund category             |
| folio_count | INTEGER   | Number of investor folios |

---

## 07_scheme_performance.csv

| Column            | Data Type | Description                  |
| ----------------- | --------- | ---------------------------- |
| amfi_code         | INTEGER   | AMFI scheme identifier       |
| return_1yr_pct    | REAL      | One-year return percentage   |
| return_3yr_pct    | REAL      | Three-year return percentage |
| return_5yr_pct    | REAL      | Five-year return percentage  |
| expense_ratio_pct | REAL      | Scheme expense ratio         |

---

## 08_investor_transactions.csv

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | AMFI scheme identifier     |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption   |
| amount_inr         | REAL      | Transaction amount         |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age group         |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakh INR  |
| payment_mode       | TEXT      | Mode of payment            |
| kyc_status         | TEXT      | KYC verification status    |

---

## 09_portfolio_holdings.csv

| Column       | Data Type | Description                     |
| ------------ | --------- | ------------------------------- |
| holding_name | TEXT      | Portfolio security name         |
| sector       | TEXT      | Industry sector                 |
| weight_pct   | REAL      | Portfolio allocation percentage |

---

## 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | DATE      | Benchmark date       |
| index_name  | TEXT      | Benchmark index name |
| index_value | REAL      | Index closing value  |

---

# Database Tables

## dim_fund

Stores master information for mutual fund schemes.

Source: 01_fund_master.csv

Primary Key: fund_id

---

## dim_date

Stores date dimension information used for reporting and analytics.

Primary Key: date_id

---

## fact_nav

Stores daily NAV history for schemes.

Source: 02_nav_history.csv

Foreign Keys:

* amfi_code → dim_fund
* date_id → dim_date

---

## fact_transactions

Stores investor transaction records.

Source: 08_investor_transactions.csv

Foreign Keys:

* amfi_code → dim_fund
* date_id → dim_date

---

## fact_performance

Stores scheme performance metrics and expense ratios.

Source: 07_scheme_performance.csv

Foreign Key:

* amfi_code → dim_fund

---

## fact_aum

Stores Assets Under Management statistics.

Source: 03_aum_by_fund_house.csv

---

## monthly_sip_inflows

Stores monthly SIP inflow data.

Source: 04_monthly_sip_inflows.csv

---

## category_inflows

Stores category-wise inflow statistics.

Source: 05_category_inflows.csv

---

## industry_folio_count

Stores industry folio count statistics.

Source: 06_industry_folio_count.csv

---

## portfolio_holdings

Stores portfolio holding allocations.

Source: 09_portfolio_holdings.csv

---

## benchmark_indices

Stores benchmark index performance history.

Source: 10_benchmark_indices.csv

---

# Data Quality Rules

1. Dates converted to standard datetime format.
2. Duplicate records removed.
3. NAV values validated to be greater than zero.
4. Transaction amounts validated to be greater than zero.
5. Transaction types standardized.
6. KYC status values validated.
7. Return metrics validated as numeric.
8. Expense ratios checked for anomaly range (0.1%–2.5%).
9. Text fields trimmed for leading/trailing spaces.
10. Cleaned datasets stored in data/processed/.

---

# Row Count Verification

All SQLite table row counts were verified against their corresponding cleaned CSV files after loading into the database.
