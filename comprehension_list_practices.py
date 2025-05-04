# 1. Create a list of numbers between 1 and 100 that are divisible by 15.
divisible_by_15 = [i for i in range(1, 101) if i % 15 == 0]
print(divisible_by_15)

# 2. Generate a list of digits from the given sentence.
text = "Room 304 is on the 5th floor and costs 1200 dollars per month."
digits = [char for char in text if char.isdigit()]
print(digits)

# 3. For each speed value in the list, if it's below 60 km/h, print "Slow zone warning".
speeds = [45, 72, 55, 80, 59]
for speed in speeds:
    if speed < 60:
        print("Slow zone warning")

# 4. Print a dictionary of employees and their salaries, only including those who earn more than 3000.
employees = ["Alice", "Bob", "Charlie", "Diana"]
salaries = [2800, 3200, 4000, 2500]

high_earners = {employees[i]: salaries[i] for i in range(len(employees)) if salaries[i] > 3000}
print(high_earners)


# 5. Convert the following for loop into a list comprehension:
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# List Comprehension Answer:
squares = [i ** 2 for i in range(10)]
print(squares)
