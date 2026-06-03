-- 1. Top 5 fund houses by AUM
SELECT fund_house, MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV by AMFI code
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Average NAV per month
SELECT strftime('%Y-%m', date) AS month,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4. Total transaction amount by state
SELECT state,
       SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Transaction count by state
SELECT state,
       COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state;

-- 6. Transaction count by KYC status
SELECT kyc_status,
       COUNT(*) AS cnt
FROM fact_transactions
GROUP BY kyc_status;

-- 7. Transaction count by payment mode
SELECT payment_mode,
       COUNT(*) AS cnt
FROM fact_transactions
GROUP BY payment_mode;

-- 8. SIP transaction count
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='Sip';

-- 9. Average expense ratio
SELECT AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;

-- 10. Top schemes by 5-year return
SELECT amfi_code,
       return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;