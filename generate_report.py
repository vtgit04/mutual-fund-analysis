"""
Bluestock Fintech — Final Report Generator
Generates Final_Report.pdf using ReportLab
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

# Setup
doc = SimpleDocTemplate("Final_Report.pdf", pagesize=A4,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=72)

styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Title'],
                              fontSize=24, textColor=colors.HexColor('#0033A0'),
                              spaceAfter=20, alignment=TA_CENTER)

heading_style = ParagraphStyle('Heading', parent=styles['Heading1'],
                                fontSize=16, textColor=colors.HexColor('#0033A0'),
                                spaceAfter=12, spaceBefore=20)

subheading_style = ParagraphStyle('Subheading', parent=styles['Heading2'],
                                   fontSize=13, textColor=colors.HexColor('#003580'),
                                   spaceAfter=8, spaceBefore=12)

body_style = ParagraphStyle('Body', parent=styles['Normal'],
                             fontSize=11, leading=16,
                             spaceAfter=8, alignment=TA_JUSTIFY)

# ─── PAGE 1: TITLE ───
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("Bluestock Fintech", title_style))
story.append(Paragraph("Mutual Fund Analysis — Capstone Project", title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("Data Engineering Internship Report", styles['Heading2']))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Prepared by: Vijay Tiwari", body_style))
story.append(Paragraph("Intern ID: PCE23AD061", body_style))
story.append(Paragraph("Duration: 7 Days | June 2026", body_style))
story.append(Paragraph("GitHub: github.com/vtgit04/mutual-fund-analysis", body_style))
story.append(PageBreak())

# ─── SECTION 1: EXECUTIVE SUMMARY ───
story.append(Paragraph("1. Executive Summary", heading_style))
story.append(Paragraph(
    "This report presents a comprehensive analysis of the Indian mutual fund industry "
    "conducted as part of a 7-day Data Engineering internship at Bluestock Fintech. "
    "The project covers end-to-end data engineering and analytics — from raw data ingestion "
    "and cleaning to SQL database design, exploratory data analysis, performance analytics, "
    "risk metrics, and an interactive Power BI dashboard.",
    body_style))
story.append(Paragraph(
    "The analysis covers 40 mutual fund schemes across 10 fund houses, spanning January 2022 "
    "to December 2025, with over 46,000 NAV records and 32,778 investor transactions. "
    "Key findings include Mirae Asset Large Cap Fund scoring a perfect 100 on the composite "
    "scorecard, 97% of SIP investors being flagged as at-risk, and industry folios doubling "
    "from 13.26 Cr to 26.12 Cr over 4 years.",
    body_style))
story.append(PageBreak())

# ─── SECTION 2: DATA SOURCES ───
story.append(Paragraph("2. Data Sources & ETL", heading_style))
story.append(Paragraph("2.1 Data Sources", subheading_style))
story.append(Paragraph(
    "The project utilised 10 datasets sourced from AMFI India, mfapi.in, and simulated "
    "investor transaction data. All datasets were loaded as CSV files and processed using "
    "Python and Pandas.",
    body_style))

data_table = Table([
    ['Dataset', 'Records', 'Description'],
    ['nav_history_clean.csv', '46,000', 'Daily NAV for 40 schemes (2022–2026)'],
    ['investor_transactions_clean.csv', '32,778', 'SIP, Lumpsum and Redemption transactions'],
    ['scheme_performance_clean.csv', '40', 'Fund performance metrics and ratings'],
    ['aum_by_fund_house_clean.csv', '-', 'AUM by fund house (quarterly)'],
    ['monthly_sip_inflows_clean.csv', '48', 'Industry SIP inflow data'],
    ['category_inflows_clean.csv', '-', 'Category-wise net inflows'],
    ['industry_folio_count_clean.csv', '-', 'Industry folio count growth'],
    ['portfolio_holdings_clean.csv', '-', 'Equity fund sector holdings'],
    ['benchmark_indices_clean.csv', '8,050', 'Nifty 50 and Nifty 100 index data'],
    ['fund_master_clean.csv', '-', 'Fund master reference data'],
], colWidths=[2.2*inch, 1.2*inch, 3*inch])

data_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0033A0')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#EEF2FF')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('PADDING', (0,0), (-1,-1), 6),
]))
story.append(data_table)
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("2.2 ETL Pipeline", subheading_style))
story.append(Paragraph(
    "Day 1 covered data ingestion — loading all 10 CSV datasets and fetching live NAV data "
    "from mfapi.in API for 6 schemes. Day 2 covered data cleaning — handling missing values, "
    "removing duplicates, standardising formats, and loading cleaned data into a SQLite star "
    "schema database using SQLAlchemy.",
    body_style))
story.append(PageBreak())

# ─── SECTION 3: EDA FINDINGS ───
story.append(Paragraph("3. EDA Findings", heading_style))
story.append(Paragraph(
    "Exploratory Data Analysis was conducted across all datasets producing 16 charts. "
    "Key findings are summarised below:",
    body_style))

eda_findings = [
    ("NAV Trend Analysis", "All 40 schemes showed consistent NAV appreciation during the 2023 bull run, with a visible correction between June–October 2024."),
    ("AUM Dominance", "SBI Mutual Fund consistently maintained the highest AUM across all years, with its lead widening each year over peers like ICICI and HDFC."),
    ("SIP All-Time High", "Monthly SIP inflows reached an all-time high in December 2025, reflecting growing retail investor participation."),
    ("Folio Growth", "Total industry folios doubled from 13.26 Cr (Jan 2022) to 26.12 Cr (Dec 2025) in just 4 years."),
    ("Demographics", "The 36–55 age group accounts for the largest share of investors, driven by mid-career wealth accumulation goals."),
]

for title, text in eda_findings:
    story.append(Paragraph(f"<b>{title}:</b> {text}", body_style))

story.append(PageBreak())

# ─── SECTION 4: PERFORMANCE ANALYSIS ───
story.append(Paragraph("4. Performance Analysis", heading_style))
story.append(Paragraph(
    "Fund performance was evaluated using multiple metrics including CAGR, Sharpe Ratio, "
    "Sortino Ratio, Alpha, Beta, Maximum Drawdown, and a composite Fund Scorecard.",
    body_style))

story.append(Paragraph("4.1 Fund Scorecard — Top 10 Funds", subheading_style))

scorecard_table = Table([
    ['Rank', 'Fund Name', 'Score', 'Sharpe', '3Y CAGR'],
    ['1', 'Mirae Asset Large Cap', '100.00', '1.45', '34.00%'],
    ['2', 'ICICI Pru Midcap', '94.44', '1.18', '31.78%'],
    ['3', 'Kotak Flexicap', '94.09', '1.31', '29.58%'],
    ['4', 'HDFC Mid-Cap Opportunities', '92.35', '1.09', '32.44%'],
    ['5', 'ICICI Pru Bluechip Direct', '91.31', '1.03', '32.49%'],
    ['6', 'Axis Midcap', '87.14', '1.00', '35.11%'],
    ['7', 'SBI Bluechip Regular', '84.10', '1.21', '30.46%'],
    ['8', 'Mirae Asset Tax Saver', '82.54', '1.23', '29.18%'],
    ['9', 'ABSL Frontline Equity', '74.89', '1.03', '28.97%'],
    ['10', 'SBI Small Cap Regular', '73.76', '0.95', '26.67%'],
], colWidths=[0.6*inch, 2.8*inch, 0.8*inch, 0.8*inch, 1*inch])

scorecard_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0033A0')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#EEF2FF')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('PADDING', (0,0), (-1,-1), 6),
]))
story.append(scorecard_table)
story.append(PageBreak())

# ─── SECTION 5: ADVANCED ANALYTICS ───
story.append(Paragraph("5. Advanced Analytics & Risk Metrics", heading_style))

story.append(Paragraph("5.1 Value at Risk (VaR)", subheading_style))
story.append(Paragraph(
    "Historical VaR (95%) was computed for all 40 funds. Small cap funds carry the highest "
    "daily VaR at -2.7%, while liquid funds have near-zero VaR. SBI Small Cap Direct Plan "
    "had the highest VaR of -2.69%.",
    body_style))

story.append(Paragraph("5.2 SIP Continuation Analysis", subheading_style))
story.append(Paragraph(
    "Out of 1,362 investors with 6+ SIP transactions, 1,332 (97%) were flagged as at-risk "
    "due to average gaps greater than 35 days between transactions. This is a critical "
    "retention concern for fund houses.",
    body_style))

story.append(Paragraph("5.3 Fund Recommendation Engine", subheading_style))
story.append(Paragraph(
    "A rule-based fund recommendation engine was built using Sharpe ratio ranking within "
    "risk grade categories. For Low risk: ICICI Pru Liquid Fund. For Moderate risk: "
    "HDFC Top 100. For High risk: Kotak Emerging Equity Fund.",
    body_style))

story.append(Paragraph("5.4 Sector Concentration (HHI)", subheading_style))
story.append(Paragraph(
    "Herfindahl-Hirschman Index was computed for all equity funds. Axis Bluechip Fund "
    "has the highest HHI of 0.297 (highly concentrated) while Kotak Flexicap and "
    "SBI Bluechip show better diversification with HHI below 0.15.",
    body_style))
story.append(PageBreak())

# ─── SECTION 6: RECOMMENDATIONS ───
story.append(Paragraph("6. Recommendations", heading_style))

recommendations = [
    "Mirae Asset Large Cap Fund is the top recommendation for moderate risk investors based on composite scorecard performance.",
    "Fund houses should implement SIP reminder systems given that 97% of investors show irregular SIP patterns.",
    "Small cap funds should carry clear risk warnings as they show daily VaR of up to -2.7%.",
    "B30 city outreach should be prioritised as T30 cities still dominate investments despite growing B30 participation.",
    "Axis Bluechip Fund investors should be made aware of high sector concentration risk with HHI of 0.297.",
]

for i, rec in enumerate(recommendations, 1):
    story.append(Paragraph(f"{i}. {rec}", body_style))

story.append(PageBreak())

# ─── SECTION 7: LIMITATIONS ───
story.append(Paragraph("7. Limitations", heading_style))

limitations = [
    "Investor transaction data is simulated and may not fully reflect real-world investor behaviour patterns.",
    "NAV data covers only 40 schemes out of 1,900+ schemes available in the Indian mutual fund industry.",
    "The fund recommendation engine uses a simple rule-based approach and does not account for investor tenure or financial goals.",
    "Power BI dashboard requires Power BI Desktop for full interactivity and cannot be embedded directly.",
    "VaR calculations are based on historical data and may not accurately predict future risk during black swan events.",
]

for i, lim in enumerate(limitations, 1):
    story.append(Paragraph(f"{i}. {lim}", body_style))

story.append(PageBreak())

# ─── SECTION 8: CONCLUSION ───
story.append(Paragraph("8. Conclusion", heading_style))
story.append(Paragraph(
    "This 7-day capstone project successfully delivered a complete end-to-end mutual fund "
    "analysis system covering data engineering, exploratory analysis, performance analytics, "
    "risk metrics, and an interactive dashboard. The project demonstrates practical skills "
    "in Python, SQL, Power BI, and financial data analysis relevant to the fintech industry.",
    body_style))
story.append(Paragraph(
    "All code, notebooks, datasets, and deliverables are available on GitHub at "
    "github.com/vtgit04/mutual-fund-analysis.",
    body_style))

# Build PDF
doc.build(story)
print("✅ Final_Report.pdf generated successfully!")