"""
data_ingestion.py
=================
Day 1 - Mutual Fund Data Analysis Project (Bluestock Fintech)
Task: Load all 10 CSV datasets, explore them, validate AMFI codes
"""

import pandas as pd
import os

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
RAW_DATA_PATH = "data/raw"

CSV_FILES = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]


# ─────────────────────────────────────────────
# STEP 3: LOAD & EXPLORE ALL 10 CSV FILES
# ─────────────────────────────────────────────
def load_and_explore_csvs():
    print("=" * 65)
    print("  STEP 3: LOADING AND EXPLORING ALL 10 CSV DATASETS")
    print("=" * 65)

    dataframes = {}

    for file in CSV_FILES:
        path = os.path.join(RAW_DATA_PATH, file)

        if not os.path.exists(path):
            print(f"\n❌ File NOT found: {path}")
            continue

        df = pd.read_csv(path)
        name = file.replace(".csv", "")
        dataframes[name] = df

        print(f"\n{'─'*60}")
        print(f"📄 FILE: {file}")
        print(f"{'─'*60}")

        # Shape
        print(f"  Shape        : {df.shape[0]} rows × {df.shape[1]} columns")

        # Data Types
        print(f"\n  Data Types:")
        for col, dtype in df.dtypes.items():
            print(f"    {col:<35} {dtype}")

        # Head
        print(f"\n  First 3 Rows:")
        print(df.head(3).to_string(index=False))

        # Anomaly Detection
        print(f"\n  🔍 Anomaly Check:")
        missing = df.isnull().sum()
        missing_cols = missing[missing > 0]
        if not missing_cols.empty:
            print(f"    ⚠️  Missing values found:")
            for col, cnt in missing_cols.items():
                print(f"       {col}: {cnt} missing ({round(cnt/len(df)*100, 1)}%)")
        else:
            print(f"    ✅ No missing values")

        duplicates = df.duplicated().sum()
        if duplicates > 0:
            print(f"    ⚠️  Duplicate rows: {duplicates}")
        else:
            print(f"    ✅ No duplicate rows")

    print(f"\n{'='*65}")
    print(f"  ✅ Loaded {len(dataframes)} / {len(CSV_FILES)} files successfully")
    print(f"{'='*65}\n")

    return dataframes


# ─────────────────────────────────────────────
# STEP 6: EXPLORE FUND MASTER
# ─────────────────────────────────────────────
def explore_fund_master(df):
    print("=" * 65)
    print("  STEP 6: FUND MASTER EXPLORATION")
    print("=" * 65)

    print(f"\n  Total Schemes       : {len(df)}")

    print(f"\n  📌 Unique Fund Houses ({df['fund_house'].nunique()}):")
    for fh in sorted(df["fund_house"].unique()):
        print(f"    - {fh}")

    print(f"\n  📌 Unique Categories ({df['category'].nunique()}):")
    for cat in sorted(df["category"].unique()):
        count = df[df["category"] == cat].shape[0]
        print(f"    - {cat:<30} ({count} schemes)")

    print(f"\n  📌 Sub-Categories ({df['sub_category'].nunique()}):")
    for sub in sorted(df["sub_category"].unique()):
        print(f"    - {sub}")

    print(f"\n  📌 Risk Categories:")
    for risk, count in df["risk_category"].value_counts().items():
        print(f"    - {risk:<25} : {count} schemes")

    print(f"\n  📌 Plans Available:")
    for plan, count in df["plan"].value_counts().items():
        print(f"    - {plan:<25} : {count} schemes")

    print(f"\n  📌 Sample AMFI Codes (first 5):")
    print(f"    {list(df['amfi_code'].head())}")
    print(f"\n  💡 AMFI Code Structure: Numeric codes assigned by AMFI India.")
    print(f"     Each code uniquely identifies one scheme variant (e.g., Direct/Regular Growth).")


# ─────────────────────────────────────────────
# STEP 7: VALIDATE AMFI CODES — DATA QUALITY
# ─────────────────────────────────────────────
def validate_amfi_codes(fund_master_df, nav_history_df):
    print("\n" + "=" * 65)
    print("  STEP 7: AMFI CODE VALIDATION — DATA QUALITY REPORT")
    print("=" * 65)

    master_codes = set(fund_master_df["amfi_code"].astype(str))
    nav_codes    = set(nav_history_df["amfi_code"].astype(str))

    missing_in_nav  = master_codes - nav_codes
    extra_in_nav    = nav_codes - master_codes
    matched         = master_codes & nav_codes

    print(f"\n  Total codes in fund_master        : {len(master_codes)}")
    print(f"  Total unique codes in nav_history : {len(nav_codes)}")
    print(f"  ✅ Matched codes                  : {len(matched)}")
    print(f"  ❌ In fund_master but MISSING in nav_history : {len(missing_in_nav)}")
    print(f"  ⚠️  In nav_history but NOT in fund_master    : {len(extra_in_nav)}")

    if missing_in_nav:
        print(f"\n  Missing codes: {list(missing_in_nav)[:5]}")
    else:
        print(f"\n  ✅ All fund_master AMFI codes have NAV history!")

    print(f"\n  📋 DATA QUALITY SUMMARY:")
    print(f"  {'─'*50}")
    if len(missing_in_nav) == 0:
        print(f"  ✅ PASS — All AMFI codes validated successfully.")
    else:
        print(f"  ⚠️  WARNING — {len(missing_in_nav)} scheme(s) have no NAV data.")
    print(f"  Completeness Score: {round(len(matched)/len(master_codes)*100, 1)}%")
    print(f"  {'─'*50}\n")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Step 3 — Load all CSVs
    dfs = load_and_explore_csvs()

    # Step 6 — Explore fund master
    if "01_fund_master" in dfs:
        explore_fund_master(dfs["01_fund_master"])

    # Step 7 — Validate AMFI codes
    if "01_fund_master" in dfs and "02_nav_history" in dfs:
        validate_amfi_codes(dfs["01_fund_master"], dfs["02_nav_history"])

    print("🎉 data_ingestion.py completed successfully!")
