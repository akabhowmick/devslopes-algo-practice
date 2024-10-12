# Create a function that takes an integer and returns the sum of its digits without converting the number to a string. Make sure you handle negatives!


def sum_of_digits(n):
    n = abs(n)
    sum = 0
    while n != 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    return sum


print(sum_of_digits(123))
print(sum_of_digits(123234))
print(sum_of_digits(-123))
