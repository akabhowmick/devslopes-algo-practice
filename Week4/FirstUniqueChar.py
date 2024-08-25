# Implement a function that returns the first non-repeating character in a string. If all characters are repeating, return null.


def first_non_repeating_char(s):
    # Create a dictionary to store the count of each character
    char_count = {}

    # Iterate over the string and update the count in the dictionary
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Iterate over the string again to find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    # If all characters are repeating, return None
    return None


# Test cases
print(first_non_repeating_char("hello"))  # Output: 'h'
print(first_non_repeating_char("aabbccddeeff"))  # Output: 'None'
print(first_non_repeating_char("aabbccddeeffgghhii"))  # Output: None
print(first_non_repeating_char(""))  # Output: None
print(first_non_repeating_char("1234567890"))  # Output: '1'
print(first_non_repeating_char("abcabcabcabc"))  # Output: 'None'