# Prompt: Write a function that takes a string and returns a dictionary with each character as the key and the number of times it appears in the string as the value.

# Extension: Modify the function to ignore spaces and punctuation, and count letters case-insensitively.

# Extension: Modify the function to return the kth most commonly occurring letter. 
# Example: ("Hello, World!", 2) would return the 2nd most common letter in the string. In this case, "o"!

def countLetter(string, k):
  # Check if k is within the range of valid indices
  if k < 1 or k > len(string):
    return "No such letter"
  
  # Remove spaces and punctuation
  string = ''.join(e for e in string if e.isalnum())
  
  # Convert string to lowercase
  string = string.lower()
  
  # Initialize dictionary to store character counts
  char_count = {}
  
  # Iterate through each character in the string
  for char in string:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  
  # Sort dictionary by values in descending order
  sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
  
  # Return the kth most common letter
  if len(sorted_char_count) < k: 
    return "No such letter"
  return list(sorted_char_count.keys())[k-1]



# Test cases
print(countLetter("Hello, World!", 2))  # Output: "o"
print(countLetter("The quick brown fox jumps over the lazy dog", 3))  # Output: "t"
print(countLetter("aaaaabbbcccccdddddeeeeee", 5))  # Output: "b"
print(countLetter("abcde", 1))  # Output: "a"
print(countLetter("abcde", 5))  # Output: "e"
print(countLetter("abcde", 6))  # Output: "No such letter"