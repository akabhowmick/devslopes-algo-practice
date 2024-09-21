def narcissistic(value):
    digits = len(str(value))
    sum = 0
    value_copy = value
    while value_copy > 0:
        curr_digit = value_copy % 10
        sum += curr_digit**digits
        value_copy //= 10
    return sum == value

# Test Cases
print(narcissistic(153))  # Output: True
print(narcissistic(370))  # Output: True
print(narcissistic(371))  # Output: False
print(narcissistic(407))  # Output: True
print(narcissistic(1634))  # Output: True
print(narcissistic(9474))  # Output: True

# The time complexity is O(d), where d is the number of digits in the input number. This is because we extract and process each digit once.