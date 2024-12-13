# Write a function that reverses an input number.


def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num



# Tests
print(reverse_number(12345))
print(reverse_number(98765))
print(reverse_number(0))
print(reverse_number(100000))
print(reverse_number(1234567890))