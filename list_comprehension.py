numbers = []

for i in range(10):
    numbers.append(i * 3)

print(numbers)

numbers_2 = [i * 3 for i in range(10)]

print(numbers_2)

person_name = "Haydar Akyurek"

for char in person_name:
    print(char.upper())

result = [char.upper() for char in person_name]
print(result)
