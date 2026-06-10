"""
Bluestock Fintech — Presentation Generator
Generates Bluestock_MF_Presentation.pptx using python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

# Colors
BLUE = RGBColor(0, 51, 160)
WHITE = RGBColor(255, 255, 255)
LIGHT_BLUE = RGBColor(238, 242, 255)
DARK = RGBColor(30, 30, 30)

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

def add_slide(prs, layout=6):
    slide_layout = prs.slide_layouts[layout]
    return prs.slides.add_slide(slide_layout)

def set_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_textbox(slide, text, left, top, width, height,
                fontsize=18, bold=False, color=DARK, align=PP_ALIGN.LEFT):
    txBox = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(fontsize)
    run.font.bold = bold
    run.font.color.rgb = color
    return txBox

def add_bullet_slide(prs, title, bullets, bg_color=WHITE):
    slide = add_slide(prs)
    set_bg(slide, bg_color)
    # Blue header bar
    shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.33), Inches(1.3))
    shape.fill.solid()
    shape.fill.fore_color.rgb = BLUE
    shape.line.fill.background()
    add_textbox(slide, title, 0.3, 0.1, 12, 1.1, fontsize=28, bold=True, color=WHITE)
    for i, bullet in enumerate(bullets):
        add_textbox(slide, f"• {bullet}", 0.5, 1.5 + i*0.75, 12, 0.7, fontsize=16, color=DARK)
    return slide

# ─── SLIDE 1: TITLE ───
slide = add_slide(prs)
set_bg(slide, BLUE)
add_textbox(slide, "Bluestock Fintech", 1, 1.5, 11, 1.2, fontsize=40, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_textbox(slide, "Mutual Fund Analysis — Capstone Project", 1, 2.8, 11, 1, fontsize=24, color=WHITE, align=PP_ALIGN.CENTER)
add_textbox(slide, "Data Engineering Internship | June 2026", 1, 3.8, 11, 0.7, fontsize=18, color=LIGHT_BLUE, align=PP_ALIGN.CENTER)
add_textbox(slide, "Vijay Tiwari | PCE23AD061", 1, 4.6, 11, 0.6, fontsize=16, color=LIGHT_BLUE, align=PP_ALIGN.CENTER)

# ─── SLIDE 2: PROBLEM & OBJECTIVE ───
add_bullet_slide(prs, "Problem & Objective", [
    "Indian MF industry manages ₹50+ Lakh Crore AUM across 1,900+ schemes",
    "Lack of unified analytics platform for fund performance comparison",
    "Investors struggle to identify best funds matching their risk appetite",
    "Objective: Build end-to-end MF analytics system for Bluestock Fintech",
    "Deliverable: Data pipeline + EDA + Performance Analytics + Dashboard",
])

# ─── SLIDE 3: DATA SOURCES ───
add_bullet_slide(prs, "Data Sources", [
    "10 datasets covering NAV history, transactions, AUM, SIP inflows",
    "46,000 NAV records across 40 schemes (Jan 2022 – Dec 2025)",
    "32,778 investor transactions (SIP, Lumpsum, Redemption)",
    "Live NAV data fetched from mfapi.in API",
    "Benchmark data: Nifty 50 and Nifty 100 index values",
])

# ─── SLIDE 4: ARCHITECTURE ───
add_bullet_slide(prs, "Project Architecture", [
    "Day 1: Data Ingestion — CSV loading + live API fetch",
    "Day 2: Data Cleaning + SQLite Star Schema Database",
    "Day 3: Exploratory Data Analysis — 16 charts",
    "Day 4: Performance Analytics — Sharpe, Sortino, Alpha/Beta, Scorecard",
    "Day 5: Power BI Dashboard — 4 interactive pages",
    "Day 6: Advanced Analytics — VaR, Rolling Sharpe, HHI, Recommender",
    "Day 7: Final Report + Presentation + GitHub Deployment",
])

# ─── SLIDE 5: EDA HIGHLIGHTS 1 ───
add_bullet_slide(prs, "EDA Highlights — Market Trends", [
    "NAV bull run clearly visible in 2023 across all equity schemes",
    "2024 market correction observed between June–October 2024",
    "SBI Mutual Fund dominates AUM with ₹12.5 Lakh Crore",
    "SIP inflows hit all-time high of ₹31,002 Cr in December 2025",
    "Mid Cap and Small Cap categories attracted highest net inflows",
])

# ─── SLIDE 6: EDA HIGHLIGHTS 2 ───
add_bullet_slide(prs, "EDA Highlights — Investor Behaviour", [
    "36–55 age group is the largest investor segment",
    "T30 cities contribute majority of SIP investments",
    "B30 cities showing growing participation — outreach is working",
    "Industry folios doubled: 13.26 Cr (2022) → 26.12 Cr (2025)",
    "Banking & Financials is the most heavily weighted sector",
])

# ─── SLIDE 7: PERFORMANCE METRICS 1 ───
add_bullet_slide(prs, "Performance Metrics — Top Funds", [
    "Mirae Asset Large Cap scored perfect 100 on composite scorecard",
    "Sharpe Ratio leader: Mirae Asset Large Cap (1.45)",
    "Sortino Ratio leader: Mirae Asset Large Cap (2.37)",
    "Highest Alpha: DSP Small Cap Fund (0.30 annualised)",
    "Lowest Max Drawdown: ICICI Pru Liquid Fund (-0.01%)",
])

# ─── SLIDE 8: PERFORMANCE METRICS 2 ───
add_bullet_slide(prs, "Performance Metrics — Risk Analysis", [
    "VaR (95%): Small cap funds carry highest daily risk at -2.7%",
    "Liquid funds safest with near-zero VaR (-0.02% to -0.03%)",
    "97% of SIP investors flagged as at-risk (gaps > 35 days)",
    "Axis Bluechip most sector-concentrated (HHI = 0.297)",
    "Kotak Flexicap best diversified equity fund (HHI = 0.136)",
])

# ─── SLIDE 9: DASHBOARD SCREENSHOTS 1 ───
add_bullet_slide(prs, "Dashboard — Industry Overview & Fund Performance", [
    "Page 1: KPI cards — AUM, SIP Inflows, Folios, Schemes",
    "Page 1: Industry AUM trend line + AUM by fund house bar chart",
    "Page 2: Return vs Risk scatter plot (bubble size = AUM)",
    "Page 2: Sortable fund scorecard table",
    "Page 2: Slicers for fund house, category, and plan",
])

# ─── SLIDE 10: DASHBOARD SCREENSHOTS 2 ───
add_bullet_slide(prs, "Dashboard — Investor Analytics & SIP Trends", [
    "Page 3: Transaction amount by state horizontal bar chart",
    "Page 3: SIP/Lumpsum/Redemption donut chart",
    "Page 3: Age group vs avg SIP amount bar chart",
    "Page 4: Dual-axis SIP inflow (bar) + Nifty 50 (line)",
    "Page 4: Category inflow heatmap matrix",
])

# ─── SLIDE 11: KEY FINDINGS ───
add_bullet_slide(prs, "Key Findings & Recommendations", [
    "Mirae Asset Large Cap is the best risk-adjusted fund overall",
    "97% SIP at-risk rate — fund houses need retention strategies",
    "Small cap investors must be warned of -2.7% daily VaR",
    "B30 city outreach is yielding results — continue expansion",
    "Industry folio doubling signals mass retail adoption of MFs",
])

# ─── SLIDE 12: THANK YOU ───
slide = add_slide(prs)
set_bg(slide, BLUE)
add_textbox(slide, "Thank You", 1, 2, 11, 1.5, fontsize=48, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_textbox(slide, "Vijay Tiwari | Data Engineering Intern", 1, 3.5, 11, 0.7, fontsize=20, color=LIGHT_BLUE, align=PP_ALIGN.CENTER)
add_textbox(slide, "github.com/vtgit04/mutual-fund-analysis", 1, 4.3, 11, 0.6, fontsize=16, color=LIGHT_BLUE, align=PP_ALIGN.CENTER)
add_textbox(slide, "Bluestock Fintech | June 2026", 1, 5, 11, 0.6, fontsize=16, color=LIGHT_BLUE, align=PP_ALIGN.CENTER)

# Save
prs.save("Bluestock_MF_Presentation.pptx")
print("✅ Bluestock_MF_Presentation.pptx generated successfully!")