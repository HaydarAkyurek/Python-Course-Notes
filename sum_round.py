numbers = [1, 3, 5, 4, 32, 56]

# Get the total sum of all numbers
result = sum(numbers)                      # 101

# Get the total sum starting from 15 (acts as initial value)
result = sum(numbers, 15)                  # 116

products = [
    {"title": "Galaxy Tab S9", "price": 1200},
    {"title": "MacBook Air M2", "price": 1500},
    {"title": "Dell XPS 13", "price": 1400},
    {"title": "Asus ZenBook", "price": 0},
]

# Total of all product prices
total_price = sum([product["price"] for product in products])    # 4100

# Count how many products have a price greater than 0
product_count = len([product for product in products if product["price"] > 0])  # 3

# Calculate the average price of non-zero priced products
result = total_price / product_count       # 1366.67

# Rounding examples with different numbers
result = round(7.3)                        # 7
result = round(7.6)                        # 8
result = round(7.5)                        # 8 (rounds to even)
result = round(2.718281, 2)                # 2.72
result = round(2.718281, 4)                # 2.7183

print(result)
