-- =============================================================================
-- 06_country_analysis.sql
-- Country-level sales analysis
-- =============================================================================

USE ecommerce_retail;

SELECT 
    country,
    COUNT(DISTINCT invoice_no) AS orders,
    SUM(revenue) AS revenue,
    ROUND(SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM clean_sales WHERE revenue > 0), 2) AS share_pct
FROM clean_sales
WHERE revenue > 0
GROUP BY country
ORDER BY revenue DESC;

-- Expected: 38 countries, UK = 84.59%
