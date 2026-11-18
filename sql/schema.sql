-- SQLite-compatible table definition. Import data/retail_sales.csv into a table named retail_sales.
CREATE TABLE IF NOT EXISTS retail_sales (
    Order_ID TEXT PRIMARY KEY,
    Order_Date TEXT,
    Customer_ID TEXT,
    Region TEXT,
    City TEXT,
    Category TEXT,
    Product TEXT,
    Quantity INTEGER,
    Unit_Price_INR REAL,
    Discount_Rate REAL,
    Sales_INR REAL,
    Cost_INR REAL,
    Profit_INR REAL,
    Payment_Method TEXT
);
