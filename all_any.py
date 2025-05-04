# Demonstrating 'all' and 'any' functions


# all() returns True only if all values are True
result = all([True, True, False])         # False: One value is False
result = all([True, True, True])          # True: All values are True

# any() returns True if at least one value is True
result = any([True, True, True])          # True: All are True
result = any([True, True, False])         # True: At least one is True
result = any([False, False, False])       # False: None are True

# Logical equivalence:
# all() ~ like 'and' => True and True and True => True
# any() ~ like 'or'  => True or False => True

numbers = [1, 2, 5, 8, 6, 52, 0]

# Check if all numbers are truthy (0 is falsy)
result = all([bool(number) for number in numbers])   # False: 0 is falsy

# Check if at least one number is truthy
result = any([bool(number) for number in numbers])   # True: many are non-zero

# Check if all numbers are even
result = all([number % 2 == 0 for number in numbers])  # False: not all are even

# Check if any number is even
result = any([number % 2 == 0 for number in numbers])  # True: 6 and 52 are even

users = ["adam", "jack", "hans"]

# Check if all usernames start with 'a'
result = all([user[0] == "a" for user in users])       # False: only one starts with 'a'

# Check if any username starts with 'a'
result = any([user[0] == "a" for user in users])       # True: 'ahmet' starts with 'a'

print(result)
