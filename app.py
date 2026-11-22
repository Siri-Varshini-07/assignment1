
import streamlit as st
import plotly.express as px
import pandas as pd

from analysis import (
    load_data,
    get_business_summary,
    get_top_cities,
    get_category_sales,
    get_region_sales,
    answer_question
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
fig1.update_traces(marker_color="#2A9D8F")

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
fig2.update_traces(marker_color="#2A9D8F")

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
fig3.update_traces(marker_color="#2A9D8F")

st.plotly_chart(fig3, use_container_width=True)

st.dataframe(region_data, use_container_width=True)

# 7. Display dataset preview
st.header("Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.caption("Business Sales Analyzer | GriidAi Internship Assignment")

st.header("Ask Your Business Data Analyst")

if "previous_question" not in st.session_state:
    st.session_state.previous_question = None

user_question = st.text_input(
    "Enter your question:",
    placeholder="Example: Which city has the highest sales?",
    key="business_question"
)

if st.button("Analyze", key="analyze_button"):
    if user_question:
        answer = answer_question(
            df,
            user_question,
            st.session_state.previous_question
        )

        st.subheader("Analysis Result")

        if isinstance(answer, pd.DataFrame):
            st.dataframe(answer, use_container_width=True)

            if "City" in answer.columns and "Sales" in answer.columns:
                fig = px.pie(
                    answer,
                    names="City",
                    values="Sales",
                    title="Sales Distribution Among Top Cities",
                    hole=0.4
                )

                fig.update_traces(
                    textinfo="percent+label",
                    textposition="inside"
                )

                st.plotly_chart(fig, use_container_width=True)

        else:
            st.write(answer)
        with st.expander("How was this answer calculated?"):

            if "city" in user_question.lower() or "cities" in user_question.lower():
                st.write("1. Selected the City and Sales columns.")
                st.write("2. Grouped records by city.")
                st.write("3. Added the sales values for each city.")
                st.write("4. Sorted cities in descending order of sales.")
                st.write("5. Displayed the requested top cities or highest-selling city.")

            elif any(
                category.lower() in user_question.lower()
                for category in df["Category"].unique()
            ):
                st.write("1. Identified the requested product category.")
                st.write("2. Filtered the dataset to include only that category.")
                st.write("3. Selected the Sales column.")
                st.write("4. Added all sales values for the selected category.")

            elif "category" in user_question.lower():
                st.write("1. Selected the Category and Sales columns.")
                st.write("2. Grouped records by product category.")
                st.write("3. Added sales values for each category.")
                st.write("4. Sorted categories by total sales.")

            elif "region" in user_question.lower():
                st.write("1. Selected the Region and Sales columns.")
                st.write("2. Grouped records by region.")
                st.write("3. Added sales values for each region.")
                st.write("4. Identified the region with the highest sales.")

            elif "year" in user_question.lower():
                st.write("1. Used the Order Date column.")
                st.write("2. Extracted the year from each order date.")
                st.write("3. Grouped records by year.")
                st.write("4. Added sales values for each year.")
                st.write("5. Identified the year with the highest sales.")

            else:
                st.write("This question is not currently supported by the analysis system.")
                st.write("Please try one of the example questions listed above.")

        st.session_state.previous_question = user_question

    else:
        st.warning("Please enter a question.")

