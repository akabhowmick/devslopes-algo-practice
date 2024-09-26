# Given an array of integers from 1 to n with one number missing, write a function to find the missing number.


def find_missing_number(lst):
    n = len(lst) + 1
    total_sum = n * (n + 1) // 2
    current_sum = sum(lst)

    return total_sum - current_sum


# Test the function
print(find_missing_number([1, 2, 4, 5, 6]))  # Output: 3
print(find_missing_number([1, 2, 3, 5, 6]))  # Output: 4
print(find_missing_number([1, 2, 3, 4, 6]))  # Output: 5
