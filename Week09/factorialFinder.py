# Prompt: Write a function that takes a non-negative integer and returns its factorial.
# Extension: Modify the function to handle large numbers by using memoization to improve efficiency.


def factorial():
    cache = {}  # Initialize memoization cache

    def factorial_helper(n):
        # Base case: factorial of 0 or 1 is 1
        if n == 0 or n == 1:
            return 1

        # Check if factorial already calculated and stored in cache
        if n in cache:
            return cache[n]

        # Calculate factorial recursively
        result = n * factorial_helper(n - 1)

        # Store calculated factorial in cache
        cache[n] = result

        return result

    return factorial_helper



# Test cases
factorial_func = factorial()
print(factorial_func(5))  # Output: 120
print(factorial_func(10))  # Output: 3628800
print(factorial_func(0))  # Output: 1
print(factorial_func(1))  # Output: 1
print(factorial_func(100))  # Output: 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862
