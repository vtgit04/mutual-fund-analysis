"""
Bluestock Fintech — Mutual Fund Analysis Dashboard
Streamlit Web App
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Bluestock MF Analysis",
    page_icon="📈",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    DATA_PATH = "data/processed/"
    nav_df = pd.read_csv(DATA_PATH + "nav_history_clean.csv")
    performance_df = pd.read_csv(DATA_PATH + "scheme_performance_clean.csv")
    sip_df = pd.read_csv(DATA_PATH + "monthly_sip_inflows_clean.csv")
    transactions_df = pd.read_csv(DATA_PATH + "investor_transactions_clean.csv")
    aum_df = pd.read_csv(DATA_PATH + "aum_by_fund_house_clean.csv")
    fund_scorecard = pd.read_csv("reports/fund_scorecard.csv")

    nav_df['date'] = pd.to_datetime(nav_df['date'])
    sip_df['month'] = pd.to_datetime(sip_df['month'])
    aum_df['date'] = pd.to_datetime(aum_df['date'])

    return nav_df, performance_df, sip_df, transactions_df, aum_df, fund_scorecard

nav_df, performance_df, sip_df, transactions_df, aum_df, fund_scorecard = load_data()

# ─── SIDEBAR ───
st.sidebar.image("https://via.placeholder.com/200x60/0033A0/FFFFFF?text=Bluestock", width=200)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Industry Overview",
    "📊 Fund Performance",
    "👥 Investor Analytics",
    "🔮 Fund Recommender",
    "📈 Monte Carlo"
])

# ─── PAGE 1: INDUSTRY OVERVIEW ───
if page == "🏠 Industry Overview":
    st.title("🏦 Bluestock Fintech — Mutual Fund Analysis")
    st.markdown("---")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total AUM", "₹81 L Cr", "+12%")
    col2.metric("SIP Inflows", "₹31,002 Cr", "+8%")
    col3.metric("Total Folios", "26.12 Cr", "+15%")
    col4.metric("Schemes", "40", "")

    st.markdown("---")

    # AUM Trend
    st.subheader("Industry AUM Trend (2022–2025)")
    aum_trend = aum_df.groupby('date')['aum_lakh_crore'].sum().reset_index()
    fig = px.line(aum_trend, x='date', y='aum_lakh_crore',
                  labels={'aum_lakh_crore': 'AUM (₹ Lakh Crore)', 'date': 'Date'})
    st.plotly_chart(fig, use_container_width=True)

    # AUM by Fund House
    st.subheader("AUM by Fund House")
    aum_by_house = aum_df.groupby('fund_house')['aum_lakh_crore'].mean().sort_values(ascending=False).reset_index()
    fig2 = px.bar(aum_by_house, x='aum_lakh_crore', y='fund_house',
                  orientation='h', color='aum_lakh_crore',
                  color_continuous_scale='Blues',
                  labels={'aum_lakh_crore': 'AUM (₹ Lakh Crore)', 'fund_house': 'Fund House'})
    st.plotly_chart(fig2, use_container_width=True)

# ─── PAGE 2: FUND PERFORMANCE ───
elif page == "📊 Fund Performance":
    st.title("📊 Fund Performance Analytics")
    st.markdown("---")

    # Filters
    col1, col2 = st.columns(2)
    fund_houses = ['All'] + sorted(performance_df['fund_house'].unique().tolist())
    categories = ['All'] + sorted(performance_df['category'].unique().tolist())
    selected_house = col1.selectbox("Fund House", fund_houses)
    selected_cat = col2.selectbox("Category", categories)

    filtered = performance_df.copy()
    if selected_house != 'All':
        filtered = filtered[filtered['fund_house'] == selected_house]
    if selected_cat != 'All':
        filtered = filtered[filtered['category'] == selected_cat]

    # Scatter plot
    st.subheader("Return vs Risk")
    fig = px.scatter(filtered, x='return_3yr_pct', y='std_dev_ann_pct',
                     size='aum_crore', color='category',
                     hover_name='scheme_name',
                     labels={'return_3yr_pct': '3Y Return (%)', 'std_dev_ann_pct': 'Std Dev (%)'},
                     title='Return vs Risk (Bubble Size = AUM)')
    st.plotly_chart(fig, use_container_width=True)

    # Scorecard table
    st.subheader("Fund Scorecard")
    merged = fund_scorecard.merge(
        performance_df[['amfi_code', 'fund_house', 'category']],
        on='amfi_code', how='left'
    )
    if selected_house != 'All':
        merged = merged[merged['fund_house'] == selected_house]
    if selected_cat != 'All':
        merged = merged[merged['category'] == selected_cat]
    st.dataframe(merged[['scheme_name', 'score', 'final_rank']].sort_values('final_rank'),
                 use_container_width=True)

# ─── PAGE 3: INVESTOR ANALYTICS ───
elif page == "👥 Investor Analytics":
    st.title("👥 Investor Analytics")
    st.markdown("---")

    # Filters
    col1, col2 = st.columns(2)
    states = ['All'] + sorted(transactions_df['state'].unique().tolist())
    tiers = ['All'] + sorted(transactions_df['city_tier'].unique().tolist())
    selected_state = col1.selectbox("State", states)
    selected_tier = col2.selectbox("City Tier", tiers)

    filtered_txn = transactions_df.copy()
    if selected_state != 'All':
        filtered_txn = filtered_txn[filtered_txn['state'] == selected_state]
    if selected_tier != 'All':
        filtered_txn = filtered_txn[filtered_txn['city_tier'] == selected_tier]

    col1, col2 = st.columns(2)

    # Transaction type donut
    txn_counts = filtered_txn['transaction_type'].value_counts().reset_index()
    fig1 = px.pie(txn_counts, names='transaction_type', values='count',
                  hole=0.4, title='Transaction Type Split')
    col1.plotly_chart(fig1, use_container_width=True)

    # Age group bar
    age_sip = filtered_txn[filtered_txn['transaction_type'] == 'Sip'].groupby('age_group')['amount_inr'].mean().reset_index()
    fig2 = px.bar(age_sip, x='age_group', y='amount_inr',
                  title='Avg SIP Amount by Age Group',
                  labels={'amount_inr': 'Avg SIP (₹)', 'age_group': 'Age Group'})
    col2.plotly_chart(fig2, use_container_width=True)

    # State bar
    state_amounts = filtered_txn.groupby('state')['amount_inr'].sum().sort_values(ascending=False).head(10).reset_index()
    fig3 = px.bar(state_amounts, x='amount_inr', y='state', orientation='h',
                  title='Top 10 States by Transaction Amount',
                  labels={'amount_inr': 'Total Amount (₹)', 'state': 'State'})
    st.plotly_chart(fig3, use_container_width=True)

# ─── PAGE 4: FUND RECOMMENDER ───
elif page == "🔮 Fund Recommender":
    st.title("🔮 Fund Recommendation Engine")
    st.markdown("---")

    risk_appetite = st.selectbox("Select Your Risk Appetite", ["Low", "Moderate", "High"])

    risk_mapping = {
        "Low": ["Low", "Below Average"],
        "Moderate": ["Moderate", "Average"],
        "High": ["Above Average", "High"]
    }

    grades = risk_mapping[risk_appetite]
    filtered = performance_df[performance_df['risk_grade'].isin(grades)]
    top3 = filtered.nlargest(3, 'sharpe_ratio')[
        ['scheme_name', 'sharpe_ratio', 'return_3yr_pct', 'expense_ratio_pct', 'risk_grade']
    ]

    st.subheader(f"Top 3 Funds for {risk_appetite} Risk Appetite")
    st.dataframe(top3, use_container_width=True)

    fig = px.bar(top3, x='scheme_name', y='sharpe_ratio',
                 color='return_3yr_pct', color_continuous_scale='Greens',
                 title='Recommended Funds by Sharpe Ratio',
                 labels={'sharpe_ratio': 'Sharpe Ratio', 'scheme_name': 'Fund'})
    st.plotly_chart(fig, use_container_width=True)

# ─── PAGE 5: MONTE CARLO ───
elif page == "📈 Monte Carlo":
    st.title("📈 Monte Carlo Simulation — 5-Year NAV Projection")
    st.markdown("---")

    top5_codes = [148567, 120843, 148569, 119551, 120505]
    top5_names = {
        148567: 'Mirae Asset Large Cap',
        120843: 'Kotak Flexicap',
        148569: 'Mirae Asset Tax Saver',
        119551: 'SBI Bluechip Regular',
        120505: 'ICICI Pru Midcap'
    }

    selected_fund = st.selectbox("Select Fund", list(top5_names.values()))
    n_sims = st.slider("Number of Simulations", 100, 1000, 500, 100)
    code = [k for k, v in top5_names.items() if v == selected_fund][0]

    fund_returns = nav_df[nav_df['amfi_code'] == code].copy()
    fund_returns['daily_return'] = fund_returns['nav'].pct_change()
    fund_returns = fund_returns.dropna(subset=['daily_return'])

    mu = fund_returns['daily_return'].mean()
    sigma = fund_returns['daily_return'].std()
    last_nav = fund_returns['nav'].iloc[-1]
    N_DAYS = 252 * 5

    with st.spinner('Running simulations...'):
        simulations = np.zeros((N_DAYS, n_sims))
        for sim in range(n_sims):
            daily_returns = np.random.normal(mu, sigma, N_DAYS)
            price_path = [last_nav]
            for r in daily_returns:
                price_path.append(price_path[-1] * (1 + r))
            simulations[:, sim] = price_path[1:]

    fig = go.Figure()
    for sim in range(min(100, n_sims)):
        fig.add_trace(go.Scatter(y=simulations[:, sim], mode='lines',
                                  line=dict(color='steelblue', width=0.5),
                                  opacity=0.1, showlegend=False))
    fig.add_trace(go.Scatter(y=np.percentile(simulations, 95, axis=1),
                              name='95th Percentile', line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(y=np.percentile(simulations, 50, axis=1),
                              name='Median', line=dict(color='orange', width=2)))
    fig.add_trace(go.Scatter(y=np.percentile(simulations, 5, axis=1),
                              name='5th Percentile', line=dict(color='red', width=2)))
    fig.update_layout(title=f'Monte Carlo — {selected_fund} (5-Year Projection)',
                      xaxis_title='Trading Days', yaxis_title='NAV (₹)',
                      template='plotly_white', height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Summary metrics
    final_navs = simulations[-1, :]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Current NAV", f"₹{last_nav:.2f}")
    col2.metric("Median 5Y NAV", f"₹{np.percentile(final_navs, 50):.2f}")
    col3.metric("Best Case (95th)", f"₹{np.percentile(final_navs, 95):.2f}")
    col4.metric("Prob of Doubling", f"{(final_navs >= last_nav * 2).mean() * 100:.1f}%")