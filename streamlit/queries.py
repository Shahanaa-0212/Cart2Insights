def get_order_status_query():
    return """
    SELECT
        order_status,
        COUNT(*) AS order_count
    FROM orders
    GROUP BY order_status
    ORDER BY order_count DESC
    """


def get_monthly_sales_query():
    return """
    SELECT
        SUBSTR(o.order_purchase_timestamp, 1, 7) AS order_month,
        SUM(oi.price + oi.freight_value) AS total_sales
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY order_month
    ORDER BY order_month
    """


def get_payment_summary_query():
    return """
    SELECT
        payment_type,
        COUNT(*) AS payment_count,
        SUM(payment_value) AS total_payment_value
    FROM payments
    GROUP BY payment_type
    ORDER BY total_payment_value DESC
    """


def get_category_sales_query():
    return """
    SELECT
        COALESCE(
            ct.product_category_name_english,
            p.product_category_name
        ) AS category,
        COUNT(oi.order_id) AS items_sold,
        SUM(oi.price) AS total_sales
    FROM order_items oi
    JOIN products p
        ON oi.product_id = p.product_id
    LEFT JOIN category_translation ct
        ON p.product_category_name = ct.product_category_name
    GROUP BY category
    ORDER BY total_sales DESC
    LIMIT 10
    """


def get_seller_performance_query():
    return """
    SELECT
        s.seller_id,
        s.seller_state,
        COUNT(DISTINCT oi.order_id) AS total_orders,
        SUM(oi.price) AS total_revenue
    FROM sellers s
    JOIN order_items oi
        ON s.seller_id = oi.seller_id
    GROUP BY s.seller_id, s.seller_state
    ORDER BY total_revenue DESC
    LIMIT 10
    """


def get_review_summary_query():
    return """
    SELECT
        review_score,
        COUNT(*) AS review_count
    FROM reviews
    GROUP BY review_score
    ORDER BY review_score
    """