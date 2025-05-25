# This script defines a generator that yields the reciprocal (1/n)
# of natural numbers starting from 1 to infinity.

# Define a generator function to yield reciprocal values
def reciprocal_numbers():
    n = 1  # Start from 1
    while True:  # Infinite loop to simulate unbounded range
        yield 1 / n  # Yield the reciprocal of the current number
        n += 1  # Increment the number for the next iteration

# This block runs only if the script is executed directly
if __name__ == "__main__":
    gen = reciprocal_numbers()  # Initialize the generator
    for _ in range(10):  # Print the first 10 reciprocals
        print(next(gen))  # Use next() to get the next value from the generator
