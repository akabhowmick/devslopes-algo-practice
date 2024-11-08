# Prompt: Write a function that takes an array and a number k as input and rotates the array to the right by k steps.


def rotate_array(nums, k):
    k = k % len(nums)
    nums[k:] = nums[len(nums) - k:] + nums[:len(nums) - k]  # Rotate the array to the right
    return nums


# Extension: Modify the function to handle negative values of k to rotate the array to the left.
def rotate_array_with_neg(nums, k):
    k = len(nums) + k % len(nums)  # Calculate the absolute value of k
    nums[k:] = nums[:len(nums) - k] + nums[len(nums) - k:]  # Rotate the array to the left
    return nums
  

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(nums, k))  # Output: [3, 4, 5, 1, 2]

nums = [1, 2, 3, 4, 5]
k = -2
print(rotate_array_with_neg(nums, k))  # Output: [5, 1, 2, 3, 4]
  
