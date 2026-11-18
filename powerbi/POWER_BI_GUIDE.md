# Power BI dashboard build guide

## 1. Load the data
1. Open Power BI Desktop.
2. Select **Get data > Text/CSV**.
3. Select `data/retail_sales.csv`.
4. Choose **Transform Data** and confirm data types:
   - Order_Date: Date
   - Quantity: Whole number
   - Unit_Price_INR, Sales_INR, Cost_INR, Profit_INR: Decimal number
   - Discount_Rate: Decimal number
5. Select **Close & Apply**.

## 2. Create a calendar table
In Modeling > New table, create:
```DAX
Calendar =
ADDCOLUMNS(
    CALENDAR(MIN(retail_sales[Order_Date]), MAX(retail_sales[Order_Date])),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month", FORMAT([Date], "MMM"),
    "Year-Month", FORMAT([Date], "YYYY-MM")
)
```
Create a relationship from `Calendar[Date]` to `retail_sales[Order_Date]`.
Sort Calendar[Month] by Calendar[Month Number].

## 3. Add measures
Copy the measures from `DAX_measures.txt` one at a time using Modeling > New measure.
The time-intelligence measures require the Calendar relationship above.

## 4. Suggested one-page dashboard
- KPI cards: Total Sales, Total Profit, Total Orders, Average Order Value, Profit Margin %.
- Line chart: Calendar[Year-Month] against Total Sales.
- Clustered column chart: Category against Total Sales and Total Profit.
- Bar chart: Region against Total Profit.
- Donut chart: Payment_Method by Total Orders.
- Slicers: Year, Region, Category, Payment_Method.

## 5. Design tips
Use a consistent 2-3 colour palette, readable titles, INR currency formatting, and avoid overcrowding.
Add a text box noting: "Dataset is synthetic and created for portfolio demonstration."
Save your Power BI file as `Retail_Sales_Dashboard.pbix` in this folder after building it.
