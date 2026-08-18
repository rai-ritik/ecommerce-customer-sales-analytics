-- =============================================================================
-- 07_time_trends.sql
-- Monthly and time-based trends
-- =============================================================================

USE ecommerce_retail;

SELECT 
    year,
    month,
    CONCAT(year, '-', LPAD(month, 2, '0')) AS year_month,
    COUNT(DISTINCT invoice_no) AS orders,
    SUM(revenue) AS revenue
FROM clean_sales
WHERE revenue > 0
GROUP BY year, month
ORDER BY year, month;

-- Expected: 13 months, Nov 2011 strongest
