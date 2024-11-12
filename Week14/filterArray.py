# Prompt: Write a function filterArray that takes an array and a callback function as input. The function should return a new array containing only the elements that satisfy the condition defined in the callback function.

# Extension: Modify the filterArray function to accept an additional argument that specifies the starting index from which to begin filtering the array.

def filterArray(arr, callback, startIndex=0):
    filtered_arr = []
    for i in range(startIndex, len(arr)):
        if callback(arr[i]):
            filtered_arr.append(arr[i])
    return filtered_arr
  
#Test cases
def isEven(num):
    return num % 2 == 0

def isOdd(num):
    return num % 2!= 0


print(filterArray([1, 2, 3, 4, 5, 6], isEven))  # Output: [2, 4, 6]
print(filterArray([1, 2, 3, 4, 5, 6], isOdd))  # Output: [1, 3, 5]
