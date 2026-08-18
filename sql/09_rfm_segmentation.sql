-- =============================================================================
-- 09_rfm_segmentation.sql
-- RFM segmentation summary
-- =============================================================================

USE ecommerce_retail;

SELECT 
    segment,
    COUNT(*) AS customers,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM rfm_customers), 2) AS customer_share_pct,
    SUM(monetary) AS revenue,
    ROUND(SUM(monetary) * 100.0 / (SELECT SUM(monetary) FROM rfm_customers), 2) AS revenue_share_pct
FROM rfm_customers
GROUP BY segment
ORDER BY revenue DESC;

-- Expected: Champions 64.61% revenue
