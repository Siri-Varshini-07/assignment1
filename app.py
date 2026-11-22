
import streamlit as st
import plotly.express as px

from analysis import (
    load_data,
    get_business_summary,
    get_top_cities,
    get_category_sales,
    get_region_sales
)

# 1. Page settings
st.set_page_config(
    page_title="Business Sales Analyzer",
    page_icon="📊",
    layout="wide"
)

# 2. Load dataset
st.title("AI-Powered Business Data Analyst")

st.write(
    "Explore business performance through sales, "
    "profit, cities, categories and regions."
)

df = load_data()

st.success("Dataset loaded successfully!")

# 3. Business summary
st.header("Business Summary")

summary = get_business_summary(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{summary['Total Sales']:,.2f}")
col2.metric("Total Profit", f"{summary['Total Profit']:,.2f}")
col3.metric("Total Orders", f"{summary['Total Orders']:,}")
col4.metric("Quantity Sold", f"{summary['Total Quantity Sold']:,}")

# 4. Top five cities
st.header("Top 5 Cities by Sales")

city_data = get_top_cities(df)

fig1 = px.bar(
    city_data,
    x="City",
    y="Sales",
    title="Top 5 Cities by Sales",
    text_auto=".2s"
)

st.plotly_chart(fig1, use_container_width=True)

st.dataframe(city_data, use_container_width=True)

# 5. Sales by category
st.header("Sales by Category")

category_data = get_category_sales(df)

fig2 = px.bar(
    category_data,
    x="Category",
    y="Sales",
    title="Category-wise Sales",
    text_auto=".2s"
)

st.plotly_chart(fig2, use_container_width=True)

st.dataframe(category_data, use_container_width=True)

# 6. Sales by region
st.header("Sales by Region")

region_data = get_region_sales(df)

fig3 = px.bar(
    region_data,
    x="Region",
    y="Sales",
    title="Region-wise Sales",
    text_auto=".2s"
)

st.plotly_chart(fig3, use_container_width=True)

st.dataframe(region_data, use_container_width=True)

# 7. Display dataset preview
st.header("Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.caption("Business Sales Analyzer | GriidAi Internship Assignment")
