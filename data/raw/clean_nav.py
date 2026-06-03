import pandas as pd

df = pd.read_csv("02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    ["amfi_code", "date"]
)

df = df.drop_duplicates()

df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

df = df[df["nav"] > 0]

df.to_csv(
    "nav_history_clean.csv",
    index=False
)

print("Cleaning completed!")
print("Rows:", len(df))