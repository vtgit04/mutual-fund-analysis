import pandas as pd

# Load data
performance_df = pd.read_csv("data/processed/scheme_performance_clean.csv")
sharpe_perf = performance_df[["amfi_code", "scheme_name", "sharpe_ratio", "risk_grade",
                               "return_3yr_pct", "expense_ratio_pct"]].copy()

# Risk appetite to risk grade mapping
risk_mapping = {
    "Low": ["Low", "Below Average"],
    "Moderate": ["Moderate", "Average"],
    "High": ["Above Average", "High"]
}

def recommend_funds(risk_appetite):
    grades = risk_mapping.get(risk_appetite, [])
    filtered = sharpe_perf[sharpe_perf["risk_grade"].isin(grades)]
    top3 = filtered.nlargest(3, "sharpe_ratio")
    return top3[["scheme_name", "sharpe_ratio", "return_3yr_pct", "expense_ratio_pct", "risk_grade"]]

if __name__ == "__main__":
    risk_appetite = input("Enter risk appetite (Low / Moderate / High): ").strip()
    result = recommend_funds(risk_appetite)
    if len(result) == 0:
        print("No funds found for this risk grade.")
    else:
        print(f"\nTop 3 Funds for {risk_appetite} Risk Appetite:")
        print("="*60)
        print(result.to_string(index=False))
