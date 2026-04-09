import streamlit as st
import pandas as pd

df = pd.read_csv("clean_products.csv")
st.title("Daraz Product Insights Dashboard")

category = st.selectbox("Select Category", df["Category"].unique())
filtered = df[df["Category"] == category]

st.write("Top Rated Products:")
st.dataframe(filtered[filtered["Rating"] >= 4.5].sort_values("Units Sold", ascending=False).head(10))
