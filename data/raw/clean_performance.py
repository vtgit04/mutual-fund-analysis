import pandas as pd

df = pd.read_csv("07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["expense_ratio_anomaly"] = (
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
)

df = df.drop_duplicates()

df.to_csv(
    "scheme_performance_clean.csv",
    index=False
)

print("Cleaning completed!")
print("Rows:", len(df))

print(
    "Expense ratio anomalies:",
    df["expense_ratio_anomaly"].sum()
)