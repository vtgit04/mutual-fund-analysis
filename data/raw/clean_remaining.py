import pandas as pd
import os

os.makedirs("../processed", exist_ok=True)

files = {
    "01_fund_master.csv": "fund_master_clean.csv",
    "03_aum_by_fund_house.csv": "aum_by_fund_house_clean.csv",
    "04_monthly_sip_inflows.csv": "monthly_sip_inflows_clean.csv",
    "05_category_inflows.csv": "category_inflows_clean.csv",
    "06_industry_folio_count.csv": "industry_folio_count_clean.csv",
    "09_portfolio_holdings.csv": "portfolio_holdings_clean.csv",
    "10_benchmark_indices.csv": "benchmark_indices_clean.csv"
}

for input_file, output_file in files.items():

    print(f"Processing {input_file}...")

    df = pd.read_csv(input_file)

    
    df = df.drop_duplicates()

    
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors="ignore")
            except:
                pass

    
    output_path = os.path.join("../processed", output_file)
    df.to_csv(output_path, index=False)

    print(f"Saved: {output_file}")

print("\nAll remaining files cleaned successfully!")