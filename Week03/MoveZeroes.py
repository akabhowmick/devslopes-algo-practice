# Write a function that takes an array of numbers and moves all zeros to the end of the array while maintaining the order of the non-zero elements.


def move_zeros(arr):
    non_zero_index = 0

    # First pass: move non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    # Second pass: fill the remaining elements with zeros
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0

    return arr

# Test the function
print(move_zeros([]))
print(move_zeros([1, 0, 1]))
print(move_zeros([1, 0, 1, 0]))
print(move_zeros([0, 0, 1, 0, 2, 3, 0, 0, 0, 4, 5, 0]))

# for i in array:
#         if i == 0:
#             array.remove(i) # Remove the element from the array
#             array.append(i) # Append the element to the end
#     return array
