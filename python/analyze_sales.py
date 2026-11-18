"""Retail Sales Analysis - beginner-friendly Python workflow.
Run from the project root: python python/analyze_sales.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_sales.csv"
OUT = ROOT / "visualizations"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order_Date"])
# Basic data quality checks
print("Rows and columns:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicate order IDs:", df["Order_ID"].duplicated().sum())

# KPI calculations
total_sales = df["Sales_INR"].sum()
total_profit = df["Profit_INR"].sum()
orders = df["Order_ID"].nunique()
units = df["Quantity"].sum()
aov = total_sales / orders
margin = total_profit / total_sales * 100

print("\n--- KEY BUSINESS KPIs ---")
print(f"Total sales: ₹{total_sales:,.2f}")
print(f"Total profit: ₹{total_profit:,.2f}")
print(f"Orders: {orders:,}")
print(f"Units sold: {units:,}")
print(f"Average order value: ₹{aov:,.2f}")
print(f"Profit margin: {margin:.2f}%")

# Monthly trend
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month", as_index=False).agg(
    Sales_INR=("Sales_INR", "sum"), Profit_INR=("Profit_INR", "sum"),
    Orders=("Order_ID", "nunique"))
monthly.to_csv(OUT / "monthly_summary.csv", index=False)

# Category, region and payment analysis
for dimension in ["Category", "Region", "Payment_Method"]:
    summary = df.groupby(dimension, as_index=False).agg(
        Sales_INR=("Sales_INR", "sum"),
        Profit_INR=("Profit_INR", "sum"),
        Orders=("Order_ID", "nunique"))
    summary.to_csv(OUT / f"{dimension.lower()}_summary.csv", index=False)
    print(f"\n{dimension} performance:\n", summary.sort_values("Sales_INR", ascending=False))

# Save charts
plt.figure(figsize=(10, 5))
plt.plot(monthly["Month"], monthly["Sales_INR"], marker="o")
plt.xticks(rotation=45, ha="right")
plt.title("Monthly Retail Sales")
plt.xlabel("Month"); plt.ylabel("Sales (INR)")
plt.tight_layout(); plt.savefig(OUT / "monthly_sales.png", dpi=160); plt.close()

category = df.groupby("Category")["Sales_INR"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
category.plot(kind="bar")
plt.title("Sales by Product Category"); plt.ylabel("Sales (INR)")
plt.xticks(rotation=20, ha="right"); plt.tight_layout()
plt.savefig(OUT / "sales_by_category.png", dpi=160); plt.close()

region = df.groupby("Region")["Profit_INR"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
region.plot(kind="bar")
plt.title("Profit by Region"); plt.ylabel("Profit (INR)")
plt.tight_layout(); plt.savefig(OUT / "profit_by_region.png", dpi=160); plt.close()

print("\nAnalysis complete. Check the visualizations/ folder.")
