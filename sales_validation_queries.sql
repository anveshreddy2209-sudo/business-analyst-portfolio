-- Total Revenue
SELECT SUM(SalesAmount) AS Total_Revenue
FROM sales_data;

-- Revenue by Region
SELECT Region, SUM(SalesAmount) AS Revenue
FROM sales_data
GROUP BY Region;

-- Average Order Value
SELECT AVG(SalesAmount) AS Avg_Order_Value
FROM sales_data;
