"""
live_nav_fetch.py
=================
Day 1 - Mutual Fund Data Analysis Project (Bluestock Fintech)
Task: Fetch live NAV for 6 schemes from mfapi.in and save as CSV
"""

import requests
import pandas as pd
import os
import time

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
BASE_URL   = "https://api.mfapi.in/mf"
OUTPUT_DIR = "data/raw"

# Step 4 + Step 5: All 6 schemes to fetch
SCHEMES = {
    "HDFC_Top100_Direct" : 125497,
    "SBI_Bluechip"       : 119551,
    "ICICI_Bluechip"     : 120503,
    "Nippon_LargeCap"    : 118632,
    "Axis_Bluechip"      : 119092,
    "Kotak_Bluechip"     : 120841,
}


# ─────────────────────────────────────────────
# FETCH ONE SCHEME
# ─────────────────────────────────────────────
def fetch_nav(scheme_name, scheme_code):
    url = f"{BASE_URL}/{scheme_code}"
    print(f"\n  Fetching: {scheme_name} (Code: {scheme_code})")
    print(f"  URL: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        meta        = data.get("meta", {})
        nav_records = data.get("data", [])

        if not nav_records:
            print(f"  ⚠️  No NAV data returned for {scheme_name}")
            return None

        df = pd.DataFrame(nav_records)
        df.columns = [c.lower() for c in df.columns]
        df["amfi_code"]        = scheme_code
        df["scheme_name"]      = meta.get("scheme_name", "N/A")
        df["fund_house"]       = meta.get("fund_house", "N/A")
        df["scheme_type"]      = meta.get("scheme_type", "N/A")
        df["scheme_category"]  = meta.get("scheme_category", "N/A")

        cols = ["amfi_code", "scheme_name", "fund_house",
                "scheme_type", "scheme_category", "date", "nav"]
        df = df[[c for c in cols if c in df.columns]]

        print(f"  ✅ Success — {len(df)} NAV records fetched")
        print(f"     Latest NAV : {df['nav'].iloc[0]} (as of {df['date'].iloc[0]})")

        return df

    except requests.exceptions.ConnectionError:
        print(f"  ❌ Connection Error — check your internet connection")
        return None
    except requests.exceptions.Timeout:
        print(f"  ❌ Timeout — API took too long to respond")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"  ❌ HTTP Error: {e}")
        return None
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return None


# ─────────────────────────────────────────────
# SAVE TO CSV
# ─────────────────────────────────────────────
def save_csv(df, scheme_name):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{OUTPUT_DIR}/live_nav_{scheme_name}.csv"
    df.to_csv(filename, index=False)
    print(f"  💾 Saved → {filename}")
    return filename


# ─────────────────────────────────────────────
# PRINT SUMMARY TABLE
# ─────────────────────────────────────────────
def print_summary(results):
    print("\n" + "=" * 65)
    print("  FETCH SUMMARY")
    print("=" * 65)
    print(f"  {'Scheme':<25} {'Code':<10} {'Records':<10} {'Latest NAV':<12} {'Status'}")
    print(f"  {'─'*25} {'─'*10} {'─'*10} {'─'*12} {'─'*10}")

    success = 0
    for name, info in results.items():
        if info["df"] is not None:
            df      = info["df"]
            nav     = df["nav"].iloc[0] if "nav" in df.columns else "N/A"
            records = len(df)
            status  = "✅ OK"
            success += 1
        else:
            nav, records, status = "N/A", 0, "❌ FAILED"
        print(f"  {name:<25} {info['code']:<10} {records:<10} {str(nav):<12} {status}")

    print(f"\n  Fetched {success} / {len(results)} schemes successfully")
    print("=" * 65)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 65)
    print("  LIVE NAV FETCH — mfapi.in")
    print("  Fetching NAV for 6 Mutual Fund Schemes")
    print("=" * 65)

    results = {}

    for name, code in SCHEMES.items():
        df = fetch_nav(name, code)
        if df is not None:
            save_csv(df, name)
        results[name] = {"code": code, "df": df}
        time.sleep(0.5)

    print_summary(results)

    # Save combined latest NAVs
    latest_navs = []
    for name, info in results.items():
        if info["df"] is not None:
            latest_navs.append(info["df"].iloc[0])

    if latest_navs:
        combined      = pd.DataFrame(latest_navs)
        combined_path = f"{OUTPUT_DIR}/live_nav_all_schemes.csv"
        combined.to_csv(combined_path, index=False)
        print(f"\n  📊 Combined latest NAV saved → {combined_path}")

    print("\n🎉 live_nav_fetch.py completed successfully!")
