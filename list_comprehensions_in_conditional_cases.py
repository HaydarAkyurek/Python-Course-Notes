numbers = [1, 4, 7, 15, 34, 56, 79]
even_numbers = []

# Using for loop to filter even numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# Using list comprehension to filter even numbers
even_numbers = [number for number in numbers if number % 2 == 0]

# Replace odd numbers with the string "odd number"
even_or_label = [number if number % 2 == 0 else "odd number" for number in numbers]

products = [4500, 1000, 0, 15350, 0, 4421]
taxed_prices = []

# Using for loop to apply tax only on non-zero values
for price in products:
    if price > 0:
        taxed_prices.append(price * 1.35)

# Using list comprehension to apply tax only on non-zero values
taxed_prices = [price * 1.35 for price in products if price > 0]

# Replace zero prices with "no tax"
taxed_or_label = [price if price > 0 else "no tax" for price in products]

print(taxed_or_label)
