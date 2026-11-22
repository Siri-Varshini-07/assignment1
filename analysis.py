
import pandas as pd

# 1. Load and prepare the dataset
def load_data():
    df = pd.read_csv("data/superstore.csv")

    df.columns = df.columns.str.strip()

    df["Order Date"] = pd.to_datetime(
        df["Order Date"], format="%m/%d/%Y", errors="coerce"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"], format="%m/%d/%Y", errors="coerce"
    )

    return df


# 2. Calculate overall business statistics
def get_business_summary(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    total_quantity = df["Quantity"].sum()

    return {
        "Total Sales": round(total_sales, 2),
        "Total Profit": round(total_profit, 2),
        "Total Orders": total_orders,
        "Total Quantity Sold": total_quantity
    }


# 3. Find the top five cities by sales
def get_top_cities(df, limit=5):
    result = (
        df.groupby("City")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(limit)
        .reset_index()
    )

    return result


# 4. Calculate sales by product category
def get_category_sales(df):
    result = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return result


# 5. Calculate sales by region
def get_region_sales(df):
    result = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return result


def answer_question(df, question, previous_question=None):

    question = question.lower().strip()

        # Handle follow-up questions
    if "top" in question and any(
        word in question for word in ["only", "show", "just"]
    ) and previous_question:

        if "city" in previous_question or "cities" in previous_question:
            question = "Show top " + question.split("top")[-1] + " cities by sales"

    # Question 1: City with highest sales
    if "city" in question and (
        "highest" in question or "most" in question
    ) and "sales" in question:

        city_sales = (
            df.groupby("City")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        highest_city = city_sales.index[0]
        highest_sales = city_sales.iloc[0]

        return (
            f"{highest_city} has the highest sales, "
            f"with total sales of {highest_sales:,.2f}."
        )

    # Question 2: Category with highest sales
    elif "category" in question and (
        "highest" in question or "most" in question
    ) and "sales" in question:

        category_sales = (
            df.groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        highest_category = category_sales.index[0]
        highest_sales = category_sales.iloc[0]

        return (
            f"{highest_category} has the highest sales, "
            f"with total sales of {highest_sales:,.2f}."
        )
    
    # Question 3: Region with highest sales
    elif "region" in question and (
        "highest" in question or "most" in question
    ) and "sales" in question:

        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        highest_region = region_sales.index[0]
        highest_sales = region_sales.iloc[0]

        return (
            f"{highest_region} region has the highest sales, "
            f"with total sales of {highest_sales:,.2f}."
        )
    
    # Question 4: Show top cities by sales
    elif ("city" in question or "cities" in question) and "sales" in question and "top" in question:

        import re

        match = re.search(r"top\s+(\d+)", question)

        limit = int(match.group(1)) if match else 5

        city_sales = (
            df.groupby("City")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(limit)
        )

        return city_sales.reset_index()

    
    # Question 5: Compare sales by category
    elif "category" in question and "sales" in question and "compare" in question:

        category_sales = (
            df.groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        return category_sales.to_string()

    
    # Question 6: Sales by year
    elif "year" in question and "sales" in question:

        yearly_sales = (
            df.groupby(df["Order Date"].dt.year)["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        highest_year = yearly_sales.index[0]
        highest_sales = yearly_sales.iloc[0]

        return (
            f"{highest_year} had the highest sales, "
            f"with total sales of {highest_sales:,.2f}."
        )
    
    # Question 7: Sales in a specific city
    elif "sales" in question and "in" in question:

        city_name = question.split("in")[-1].strip().title()

        city_data = df[df["City"].str.lower() == city_name.lower()]

        if not city_data.empty:
            total_sales = city_data["Sales"].sum()

            return (
                f"Total sales in {city_name} are "
                f"{total_sales:,.2f}."
            )
        else:
            return f"Sorry, I couldn't find sales data for {city_name}."
    # Question 8: Sales for a specific category
    elif "sales" in question and any(
        category.lower() in question
        for category in df["Category"].unique()
    ):

        category_name = next(
            category for category in df["Category"].unique()
            if category.lower() in question
        )

        category_data = df[
            df["Category"].str.lower() == category_name.lower()
        ]

        total_sales = category_data["Sales"].sum()

        return (
            f"Total sales for {category_name} are "
            f"{total_sales:,.2f}."
        )
    
    else:
        return (
            "I'm unable to answer that question yet.\n\n"
            "You can try questions like:\n"
            "1. Which city has the highest sales?\n"
            "2. Which category has the highest sales?\n"
            "3. Which region has the highest sales?\n"
            "4. Show top 5 cities by sales.\n"
            "5. Compare sales by category.\n"
            "6. Which year had the highest sales?\n\n"
            "Please try rephrasing your question."
        )


# 6. Run the analysis
if __name__ == "__main__":

    df = load_data()

    print("\n===== BUSINESS SUMMARY =====")
    summary = get_business_summary(df)

    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n===== TOP 5 CITIES BY SALES =====")
    print(get_top_cities(df))

    print("\n===== SALES BY CATEGORY =====")
    print(get_category_sales(df))

    print("\n===== SALES BY REGION =====")
    print(get_region_sales(df))

    #question = "Which city has the highest sales?"

    #question = "Which category has the highest sales?"

    #question = "Which region has the highest sales?"

    #question = "Show top 3 cities by sales"

    #question = "Compare sales by category"

    question1 = "Show top 5 cities by sales"
    answer1 = answer_question(df, question1)

    print("\nQUESTION:", question1)
    print("ANSWER:", answer1)

    question2 = "Show only top 3"
    answer2 = answer_question(df, question2, question1)

    print("\nFOLLOW-UP:", question2)
    print("ANSWER:", answer2)


