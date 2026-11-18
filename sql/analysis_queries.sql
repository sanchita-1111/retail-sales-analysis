-- 1. Overall KPIs
SELECT
  ROUND(SUM(Sales_INR), 2) AS total_sales_inr,
  ROUND(SUM(Profit_INR), 2) AS total_profit_inr,
  COUNT(DISTINCT Order_ID) AS total_orders,
  SUM(Quantity) AS units_sold,
  ROUND(AVG(Sales_INR), 2) AS average_order_value
FROM retail_sales;

-- 2. Monthly sales and profit trend
SELECT strftime('%Y-%m', Order_Date) AS month,
       ROUND(SUM(Sales_INR), 2) AS sales_inr,
       ROUND(SUM(Profit_INR), 2) AS profit_inr,
       COUNT(DISTINCT Order_ID) AS orders
FROM retail_sales
GROUP BY month
ORDER BY month;

-- 3. Category performance
SELECT Category, ROUND(SUM(Sales_INR),2) AS sales_inr,
       ROUND(SUM(Profit_INR),2) AS profit_inr,
       SUM(Quantity) AS units_sold
FROM retail_sales
GROUP BY Category
ORDER BY sales_inr DESC;

-- 4. Region performance
SELECT Region, ROUND(SUM(Sales_INR),2) AS sales_inr,
       ROUND(SUM(Profit_INR),2) AS profit_inr,
       COUNT(DISTINCT Order_ID) AS orders
FROM retail_sales
GROUP BY Region
ORDER BY profit_inr DESC;

-- 5. Top 10 products by revenue
SELECT Product, Category, SUM(Quantity) AS units_sold,
       ROUND(SUM(Sales_INR),2) AS sales_inr
FROM retail_sales
GROUP BY Product, Category
ORDER BY sales_inr DESC
LIMIT 10;

-- 6. Payment method preference
SELECT Payment_Method, COUNT(DISTINCT Order_ID) AS orders,
       ROUND(SUM(Sales_INR),2) AS sales_inr
FROM retail_sales
GROUP BY Payment_Method
ORDER BY orders DESC;

-- 7. Customers with highest lifetime sales (within this sample)
SELECT Customer_ID, COUNT(DISTINCT Order_ID) AS orders,
       ROUND(SUM(Sales_INR),2) AS lifetime_sales_inr
FROM retail_sales
GROUP BY Customer_ID
ORDER BY lifetime_sales_inr DESC
LIMIT 10;
