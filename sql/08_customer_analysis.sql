-- =============================================================================
-- 08_customer_analysis.sql
-- Customer-level analysis
-- =============================================================================

USE ecommerce_retail;

SELECT 
    customer_id,
    COUNT(DISTINCT invoice_no) AS orders,
    SUM(revenue) AS revenue,
    MIN(invoice_date) AS first_purchase,
    MAX(invoice_date) AS last_purchase
FROM clean_sales
WHERE revenue > 0 AND customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 20;

-- Expected: 4338 customers, top = 14646
