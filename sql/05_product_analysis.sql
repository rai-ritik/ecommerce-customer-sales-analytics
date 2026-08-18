-- =============================================================================
-- 05_product_analysis.sql
-- Product-level sales analysis
-- =============================================================================

USE ecommerce_retail;

SELECT 
    stock_code,
    ANY_VALUE(description) AS description,
    COUNT(DISTINCT invoice_no) AS orders,
    SUM(quantity) AS units_sold,
    SUM(revenue) AS revenue
FROM clean_sales
WHERE revenue > 0
GROUP BY stock_code
ORDER BY revenue DESC
LIMIT 20;

-- Expected: 3922 products, top = DOTCOM POSTAGE
