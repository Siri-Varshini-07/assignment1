
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
