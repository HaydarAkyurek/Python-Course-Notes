#1. Filtering negative numbers
numbers = [1, 3, 5, -4, -3]

# Get only the negative numbers using filter and lambda
result = list(filter(lambda x: x < 0, numbers))
print(result)  # Output: [-4, -3]


#  2. Filtering odd numbers
# Get only the odd numbers
result = list(filter(lambda x: x % 2 == 1, numbers))
print(result)  # Output: [1, 3, 5]

#  3. Filter names that start with 'a' and convert them to uppercase
names = ["chris", "alice", "anna", "yigit", "susan"]

# Filter names starting with 'a'
filtered_names = list(filter(lambda name: name[0] == 'a', names))

# Convert them to uppercase
result = list(map(lambda name: name.upper(), filtered_names))
print(result)  # Output: ['ALICE', 'ANNA']

#4. Filter users who have posts and get their usernames
users = [
    {"username": "johndoe", "posts": ["post 1", "post 2"]},
    {"username": "janedoe", "posts": []},
    {"username": "mikebrown", "posts": ["post 1", "post 2", "post 3"]},
]

# Filter users who have at least one post
active_users = list(filter(lambda user: len(user["posts"]) > 0, users))

# Get usernames of those users
result = list(map(lambda user: user["username"], active_users))
print(result)  # Output: ['johndoe', 'mikebrown']

#Same with list comprehension and uppercase usernames
result = [user["username"].upper() for user in users if len(user["posts"]) > 0]
print(result)  # Output: ['JOHNDOE', 'MIKEBROWN']
