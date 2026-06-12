def calculate_discount(purchase_amount: float) -> float:
    """
    Calculate discount based on purchase amount.
    - 10% discount for VIP customers (>= 50,000,000 VND)
    - No discount for normal customers
    """
    discount_rate = 0.0

    if purchase_amount >= 50000000:
        discount_rate = 0.1
    else:
        discount_rate = 0.0

    return discount_rate
