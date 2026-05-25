"""
Order < 10$ → +3$ service fee, >= 10$ && <=50 → no service fee
Order > 50$ → free delivery + free service fee (no peak hour fee)
Order >=10$, <50$ → no fee (peak hour +2$)
Delivery_time = peak hour → +2$
Premium member = Free delivery
Delivery_distance > 20 =  unavailable

"""

def compute_food_delivery(
    amount_orders,
    isPeakHours,
    isMembership,
    delivery_distance,
):
    if delivery_distance > 20:
        return -1
    if amount_orders > 50:
        return amount_orders
    if amount_orders < 10:
       amount_orders = amount_orders + 3
    if isPeakHours == True:
        if isMembership == False and amount_orders <= 50:
            amount_orders = amount_orders + 2
    return amount_orders