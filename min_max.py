numbers = [1, 4, 6, 32, 23, 12]
letters = ['a', 'c', 'v', 'z']
names = ['john', 'alex', 'sara', 'michael']

# Get the smallest number from the list
result = min(numbers)             # 1

# Get the largest number from the list
result = max(numbers)             # 32

# Get the first letter in alphabetical order
result = min(letters)             # 'a'

# Get the last letter in alphabetical order
result = max(letters)             # 'z'

# Get the name that comes first alphabetically
result = min(names)               # 'alex'

# Get the name that comes last alphabetically
result = max(names)               # 'sara'

# Get the shortest name length
result = min([len(name) for name in names])   # 4

# Get the longest name length
result = max([len(name) for name in names])   # 7

# Get the longest name by actual name (not just length)
result = max(names, key = lambda name: len(name))   # 'michael'

# Get the shortest name
result = min(names, key = lambda name: len(name))   # 'john'

products = [
    {"title": "iPhone 14", "price": 950},
    {"title": "Galaxy S24", "price": 870},
    {"title": "Pixel 8", "price": 800}
]

# Get the product with the lowest price
result = min(products, key = lambda product: product["price"])  # {"title": ..., "price": ...}

# Get the title of the most expensive product
result = max(products, key = lambda product: product["price"])["title"]  # 'iPhone 14'

max_price = 0

# Classic loop to find the highest price
for product in products:
    if product["price"] > max_price:
        max_price = product["price"]

print(max_price)     # 950

print(result)        # Depends on the last assigned result
