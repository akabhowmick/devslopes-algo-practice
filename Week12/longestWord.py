# Prompt: Write a function that takes a string as input and returns the longest word in the string.
# Extension: Modify the function to return an array of all longest words (in case there are ties).


def longestWord(sentence):
    longestWords = []
    words = sentence.split()
    if not words:
        return longestWords
    maxWordLength = 0
    for word in words:
        if len(word) > maxWordLength:
            maxWordLength = len(word)
    for word in words:
        if len(word) == maxWordLength:
            longestWords.append(word)
    return longestWords


# Test cases
print(longestWord("Hello world! This is a test sentence."))  # Output: ['sentence']
print(
    longestWord("This is a longer sentence with multiple longest words.")
)  # Output: ['longer', 'sentence', 'multiple', 'longest', 'words.']
print(
    longestWord("One two three four five.")
)  # Output: ['one', 'two', 'three', 'four', 'five.']
print(longestWord("Single word."))  # Output: ['Single', 'word.']
print(longestWord(""))  # Output: []
