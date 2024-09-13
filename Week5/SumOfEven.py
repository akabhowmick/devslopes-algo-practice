# Prompt: Write a function that takes a list of numbers and returns the sum of all even numbers in the list.
# Extension: Modify the function to return both the sum of even numbers and the sum of odd numbers.

def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:  # Check if number is even
            even_sum += num
        else:  # Check if number is odd
            odd_sum += num
    return even_sum, odd_sum
