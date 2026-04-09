# cleaning.py
import pandas as pd

# Load Raw Data
df = pd.read_csv("products.csv")

# Cleaning Functions
def clean_sold(s):
    if isinstance(s, str):
        s = s.strip()
        if "K" in s:
            return float(s.replace("K sold", "")) * 1000
        elif "sold" in s:
            return float(s.replace("sold", ""))
    return 0

def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Clean Price
    df["Price"] = df["Price"].str.replace("Rs. ", "").str.replace(",", "")
    df["Price"] = df["Price"].replace(["No Price", ""], "0").astype(float)

    # Clean Units Sold
    df["Units Sold"] = df["Units Sold"].apply(clean_sold).astype(int)

    # Feature Engineering
    df["Revenue"] = df["Price"] * df["Units Sold"]

    # Remove extreme outliers (top 1%)
    df = df[df["Price"] < df["Price"].quantile(0.99)]

    return df

# Apply Cleaning
df = clean_data(df)

# Save Cleaned Data
df.to_csv("clean_products.csv", index=False)

print("Data cleaning completed. Cleaned file saved as 'clean_products.csv'.")