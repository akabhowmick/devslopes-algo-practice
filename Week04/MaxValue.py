# Implement a function that returns the first non-repeating character in a string. If all characters are repeating, return null.


def maxValue(array):
    max_value = float("-inf")
    for i in range(len(array)):
        if array[i] > max_value:
            max_value = array[i]
    return max_value


def maxValueIndex(array):
    max_value = float("-inf")
    max_index = -1
    for i in range(len(array)):
        if array[i] > max_value:
            max_value = array[i]
            max_index = i
    return max_index


# Test Cases
print("the maximum value is: ", maxValue([1, 2, 3, 4, 5]))  # Output: 5
print("the maximum value is: ", maxValue([5, 5, 5, 5, 5]))  # Output: 5
print(
    "the maximum value is: ", maxValue([1, 2, 3, 4, 5, 6, 10, 8, 9, 10])
)  # Output: 10
print("the maximum value is: ", maxValue([-1, -2, -3, -4, -5]))  # Output: -1

print("the maximum value index is", maxValueIndex([1, 2, 3, 4, 5]))  # Output: 4
print("the maximum value index is", maxValueIndex([5, 5, 5, 5, 5]))  # Output: 0
print(
    "the maximum value index is", maxValueIndex([1, 2, 3, 4, 5, 10, 7, 8, 9])
)  # Output: 5
print("the maximum value index is", maxValueIndex([-1, -2, -3, -4, -5]))  # Output: 0
