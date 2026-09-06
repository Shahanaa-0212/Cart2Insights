import streamlit as st
import pandas as pd

from database import get_connection
from queries import (
    get_order_status_query,
    get_monthly_sales_query,
    get_payment_summary_query,
    get_category_sales_query,
    get_seller_performance_query,
    get_review_summary_query
)

from utils import format_currency, format_number, calculate_aov

st.set_page_config(
    page_title="Cart2Insights",
    page_icon="🛒",
    layout="wide"
)

conn = get_connection()

orders = pd.read_sql_query(
    "SELECT * FROM orders",
    conn
)

order_items = pd.read_sql_query(
    "SELECT * FROM order_items",
    conn
)

payments = pd.read_sql_query(
    "SELECT * FROM payments",
    conn
)

reviews = pd.read_sql_query(
    "SELECT * FROM reviews",
    conn
)

status_data = pd.read_sql_query(
    get_order_status_query(),
    conn
)

monthly_sales = pd.read_sql_query(
    get_monthly_sales_query(),
    conn
)

payment_summary = pd.read_sql_query(
    get_payment_summary_query(),
    conn
)

category_sales = pd.read_sql_query(
    get_category_sales_query(),
    conn
)

seller_performance = pd.read_sql_query(
    get_seller_performance_query(),
    conn
)

review_summary = pd.read_sql_query(
    get_review_summary_query(),
    conn
)

total_orders = orders["order_id"].nunique()

total_sales = order_items["price"].sum()

average_order_value = calculate_aov(
    total_sales,
    total_orders
)

average_review = reviews["review_score"].mean()

st.title("Cart2Insights")
st.subheader("Decoding E-Commerce Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Orders",
    format_number(total_orders)
)

col2.metric(
    "Total Sales",
    format_currency(total_sales)
)

col3.metric(
    "Average Order Value",
    format_currency(average_order_value)
)

col4.metric(
    "Average Review Score",
    f"{average_review:.2f}"
)

st.header("Order Status Distribution")

st.bar_chart(
    status_data.set_index("order_status")["order_count"]
)

st.header("Monthly Sales Trend")

st.line_chart(
    monthly_sales.set_index("order_month")["total_sales"]
)

st.header("Payment Method Analysis")

st.bar_chart(
    payment_summary.set_index("payment_type")["total_payment_value"]
)

st.header("Top Product Categories")

st.bar_chart(
    category_sales.set_index("category")["total_sales"]
)

st.header("Top Sellers")

st.dataframe(
    seller_performance,
    use_container_width=True
)

st.header("Review Score Distribution")

st.bar_chart(
    review_summary.set_index("review_score")["review_count"]
)

conn.close()