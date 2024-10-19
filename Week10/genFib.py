# Write a function that takes a number n and returns the first n numbers in the Fibonacci sequence.
# Extension: Modify the function to return the Fibonacci sequence as a comma-separated string.

def fibonacci_sequence(n):
    if n <= 0:
        return ""
    elif n == 0:
       return "0"
    elif n == 1:
        return "0"
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return ", ".join(map(str, fib_sequence))
  
print(fibonacci_sequence(10))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print(fibonacci_sequence(5))   # Output: 0, 1, 1, 2, 3
print(fibonacci_sequence(0))   # Output: ''
print(fibonacci_sequence(1))   # Output: 0
print(fibonacci_sequence(2))   # Output: 0, 1
print(fibonacci_sequence(3))   # Output: 0, 1, 1