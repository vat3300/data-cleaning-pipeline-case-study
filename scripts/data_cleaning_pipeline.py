import pandas as pd

# Step 1: Load raw data
df = pd.read_csv("../raw_data/raw_operational_data.csv")

# Step 2: Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Step 3: Handle missing values
df["customer_name"] = df["customer_name"].fillna("Unknown")
df["region"] = df["region"].fillna("Not Specified")
df["order_amount"] = df["order_amount"].fillna(0)

# Step 4: Standardize text values
df["status"] = df["status"].str.capitalize()

# Step 5: Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Step 6: Remove duplicate records
df = df.drop_duplicates()

# Step 7: Handle invalid order amounts
df = df[df["order_amount"] >= 0]

# Step 8: Validation checks
assert df["order_id"].isnull().sum() == 0, "Order ID contains null values"

# Step 9: Save cleaned data
df.to_csv("../cleaned_data/cleaned_operational_data.csv", index=False)

print("Data cleaning pipeline executed successfully.")
