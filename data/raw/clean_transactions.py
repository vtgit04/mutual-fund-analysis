import pandas as pd

df = pd.read_csv("08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"].isin(valid_types)
]

df = df[df["amount_inr"] > 0]

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

df = df.drop_duplicates()

df.to_csv(
    "investor_transactions_clean.csv",
    index=False
)

print("Cleaning completed!")
print("Rows:", len(df))