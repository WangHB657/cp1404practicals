"""
Function get_positive_number(prompt)
    get value
    if value is digit and value >= 0
    return value
    else
        print "Invalid number of items! Please enter a valid positive integer."

total_price = 0
number_items = get_positive_number("Number of items: ")
for item in range(number_items)
    get price
    if float(price) >= 0
        total_price = total_price + float(price)
    else
        print "Invalid price! Please enter a valid positive price."
        get price

if total_price > 100
    discounted_price = total_price * 0.9
    print number_items, discounted_price
else
    print number_items, total_price
"""


def get_positive_number(prompt):
    value = input(prompt)
    if value.isdigit() and int(value) >= 0:
        return int(value)
    else:
        print("Invalid number of items! Please enter a valid positive integer.")


DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9
total_price = 0 
number_items = get_positive_number("Number of items: ")
for item in range(number_items):
    price = input(f"Price of item {item + 1}: $")
    if float(price) >= 0:
        total_price += float(price)
    else:
        print("Invalid price! Please enter a valid positive price.")
        price = input(f"Price of item {item + 1}: $")

if total_price > DISCOUNT_THRESHOLD:
    discounted_price = total_price * DISCOUNT_RATE
    print(f"Total price for {number_items} items is ${discounted_price:.2f} (with a 10% discount).")
else:
    print(f"Total price for {number_items} items is ${total_price:.2f}")
