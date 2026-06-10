# 🏦 Bluestock Fintech — Mutual Fund Analysis Capstone

A complete end-to-end mutual fund data analysis project built during my Data Engineering internship at Bluestock Fintech. Covers data ingestion, cleaning, SQL database design, EDA, performance analytics, advanced risk metrics, and an interactive Power BI dashboard.

---

## 📁 Project Structure

my_project/
├── data/
│   ├── raw/                  # Original CSV datasets
│   └── processed/            # Cleaned CSV files
├── charts/                   # All exported chart PNGs
├── EDA_Analysis.ipynb        # Day 3: Exploratory Data Analysis
├── Performance_Analytics.ipynb # Day 4: Fund Performance Metrics
├── Advanced_Analytics.ipynb  # Day 6: Risk Metrics & Advanced Analysis
├── recommender.py            # Fund recommendation engine
├── fund_scorecard.csv        # Composite fund scorecard (0-100)
├── alpha_beta.csv            # Alpha & Beta for all funds
├── var_cvar_report.csv       # VaR & CVaR risk report
├── bluestock_mf_dashboard.pbix # Power BI Dashboard
├── Dashboard.pdf             # Exported dashboard PDF
└── requirements.txt          # Python dependencies
---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/vtgit04/mutual-fund-analysis.git
cd mutual-fund-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Jupyter Notebook
```bash
python -m notebook
```

---

## 📊 How to Run

### EDA Analysis
Open `EDA_Analysis.ipynb` and run all cells — generates 16 charts in the `charts/` folder.

### Performance Analytics
Open `Performance_Analytics.ipynb` and run all cells — generates Sharpe, Sortino, Alpha/Beta, Scorecard and Benchmark charts.

### Advanced Analytics
Open `Advanced_Analytics.ipynb` and run all cells — generates VaR, Rolling Sharpe, Cohort, SIP Continuation and HHI charts.

### Fund Recommender
```bash
python recommender.py
```
Enter risk appetite (Low / Moderate / High) when prompted.

---

## 🗄️ Database

SQLite star schema database with 8 dimension and fact tables connected on `amfi_code` and `date`.

---

## 📈 Dashboard

Open `bluestock_mf_dashboard.pbix` in Power BI Desktop to explore the interactive dashboard with 4 pages:
- **Page 1:** Industry Overview
- **Page 2:** Fund Performance
- **Page 3:** Investor Analytics
- **Page 4:** SIP & Market Trends

---

## 🔑 Key Findings

- Mirae Asset Large Cap Fund scored a perfect 100 on the composite fund scorecard
- 97% of SIP investors flagged as at-risk due to irregular transaction gaps
- Small cap funds carry the highest daily VaR at -2.7%
- Industry folios doubled from 13.26 Cr to 26.12 Cr in 4 years
- SBI dominates AUM with ₹12.5L Cr across all years

---

## 👨‍💻 Author

**Vijay Tiwari**
Data Engineering Intern — Bluestock Fintech
GitHub: [@vtgit04](https://github.com/vtgit04)