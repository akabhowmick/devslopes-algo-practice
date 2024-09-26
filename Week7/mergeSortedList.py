# "Prompt: Write a function that takes two sorted lists of numbers and returns a single sorted list containing all elements from both lists.
# Extension: Modify the function to merge the lists without using any built-in sorting functions."

def merge_sorted_lists(list1, list2):
    merged_list = []
    index1 = 0
    index2 = 0

    # Continue merging until we reach the end of either list
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1

    # Append any remaining elements from the non-exhausted list
    merged_list.extend(list1[index1:])
    merged_list.extend(list2[index2:])

    return merged_list
  

# Test the function
print(merge_sorted_lists([1, 3, 5, 7], [2, 4, 6, 8]))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(merge_sorted_lists([1, 3, 5, 7], [3, 5, 7, 9]))  # Output: [1, 3, 3, 5, 5, 7, 7, 9]
print(merge_sorted_lists([], [2, 4, 6, 8]))  # Output: [2, 4, 6, 8]
print(merge_sorted_lists([1, 2, 3, 4], []))  # Output: [1, 2, 3, 4]