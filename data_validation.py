import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Calculate Total Revenue
total_revenue = df["SalesAmount"].sum()
print("Total Revenue:", total_revenue)

# Calculate Average Order Value
avg_order_value = df["SalesAmount"].mean()
print("Average Order Value:", avg_order_value)

# Revenue by Region
revenue_by_region = df.groupby("Region")["SalesAmount"].sum()
print("Revenue by Region:\n", revenue_by_region)
