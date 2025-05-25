import time  # Import the time module to measure execution time

# This is the outermost function: it takes an argument to configure the decorator
def speed_test_with_param(repeat_count):  # repeat_count is how many times to run the function
    def decorator(fn):  # This is the actual decorator that wraps the target function
        def inner(*args, **kwargs):  # Inner function to execute the target function
            total_time = 0  # Variable to store total execution time
            result = None  # To store the result of the function
            for i in range(repeat_count):  # Repeat the function n times
                print(f"Running {fn.__name__}, iteration {i+1}")  # Show function name and iteration
                start_time = time.perf_counter()  # Start time
                result = fn(*args, **kwargs)  # Call the original function
                end_time = time.perf_counter()  # End time
                elapsed = end_time - start_time  # Calculate elapsed time
                print(f"Time for run {i+1}: {elapsed:.4f} seconds")  # Show time for this run
                total_time += elapsed  # Add to total time
            avg_time = total_time / repeat_count  # Calculate average time
            print(f"Average execution time for {fn.__name__}: {avg_time:.4f} seconds")  # Show average
            return result  # Return the result of the last function call
        return inner  # Return the inner function (decorated version)
    return decorator  # Return the decorator itself

# Example function to test: sum of generator expression
@speed_test_with_param(3)  # Run this function 3 times and measure time
def sum_gen():    
    return sum((x for x in range(10_000_000)))  # Generator-based sum

# Example function to test: sum of list
@speed_test_with_param(3)  # Also run this 3 times
def sum_list():
    return sum([x for x in range(10_000_000)])  # List-based sum

# Execute both functions
print("Result from sum_gen():", sum_gen())  # Print the result of sum_gen
print("Result from sum_list():", sum_list())  # Print the result of sum_list
