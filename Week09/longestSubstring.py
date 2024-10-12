# Write a function that takes a string and returns the length of the longest substring without repeating characters.

def longest_substring_length(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    visited_chars = {}

    # Iterate through the string
    for i in range(len(s)):
        # If the current character is already visited and its index is within the current substring, update the start index of the substring
        if s[i] in visited_chars and visited_chars[s[i]] >= current_length:
            current_length = i - visited_chars[s[i]]

        # Update the maximum length and the visited character's index
        max_length = max(max_length, current_length + 1)
        visited_chars[s[i]] = i

    return max_length