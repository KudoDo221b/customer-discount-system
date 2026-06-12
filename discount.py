def calculate_discount(total_amount, current_order_amount=0):
    if total_amount + current_order_amount >= 50000000:
        return 0.1
    return 0
