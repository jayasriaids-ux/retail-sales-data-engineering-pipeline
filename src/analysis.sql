-- 1. Total sales
SELECT SUM(total_sales) AS total_revenue
FROM retail_sales;

-- 2. Total orders
SELECT COUNT(*) AS total_orders
FROM retail_sales;

-- 3. Sales by product
SELECT product_name, SUM(total_sales) AS product_revenue
FROM retail_sales
GROUP BY product_name
ORDER BY product_revenue DESC;

-- 4. Sales by region
SELECT region, SUM(total_sales) AS regional_revenue
FROM retail_sales
GROUP BY region
ORDER BY regional_revenue DESC;