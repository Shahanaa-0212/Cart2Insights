def format_currency(value):
    return f"₹{value:,.2f}"


def format_number(value):
    return f"{value:,.0f}"


def calculate_aov(total_sales, total_orders):
    if total_orders == 0:
        return 0
    return total_sales / total_orders