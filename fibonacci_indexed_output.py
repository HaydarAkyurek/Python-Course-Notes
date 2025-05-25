# This script compares two implementations of the Fibonacci sequence:
# 1. A regular function that returns a full list of Fibonacci numbers
# 2. A generator that yields Fibonacci numbers one by one
# It also prints every 1000th number to show selective sampling.

import time  # Import time module for performance measurement

# Define a standard function to compute Fibonacci numbers up to 'n'
def fibonacci_normal(n):
    fib = [0, 1]  # Initialize list with first two Fibonacci numbers
    for i in range(2, n):  # Loop from the 3rd element to n
        fib.append(fib[i - 1] + fib[i - 2])  # Add the next Fibonacci number
    return fib  # Return the full list

# Define a generator function for Fibonacci sequence
def fibonacci_generator():
    a, b = 0, 1  # Start with 0 and 1
    while True:  # Infinite loop to continuously generate values
        yield a  # Yield the current value of 'a'
        a, b = b, a + b  # Update values for the next step

# Main block to execute the performance comparison
if __name__ == "__main__":
    N = 10000  # Define how many Fibonacci numbers to generate

    # --- Test the normal function ---
    print("Normal function:")
    start = time.time()  # Record start time
    normal_result = fibonacci_normal(N)  # Generate Fibonacci numbers
    end = time.time()  # Record end time
    print(f"Time: {end - start:.6f} sec")  # Print the time taken

    # Print every 1000th Fibonacci number using list indexing
    print("Sample (every 1000th value):")
    for i in range(1000, N+1, 1000):  # From 1000 to N, in steps of 1000
        print(f"F({i}) = {normal_result[i - 1]}")  # Print value at that index

    # --- Test the generator function ---
    print("\nGenerator function:")
    start = time.time()  # Start timing again
    gen = fibonacci_generator()  # Initialize generator
    for i in range(1, N + 1):  # Loop to get the first N Fibonacci numbers
        num = next(gen)  # Fetch the next number
        if i % 1000 == 0:  # If index is a multiple of 1000
            print(f"F({i}) = {num}")  # Print the value
    end = time.time()  # End timing
    print(f"Time: {end - start:.6f} sec")  # Print time taken
