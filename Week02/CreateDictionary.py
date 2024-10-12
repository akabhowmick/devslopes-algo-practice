# Implement a function that takes a string and returns an object with the counts of vowels and consonants.


def create_count(str):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_count = 0
    consonant_count = 0

    for char in str:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    return {"vowels": vowel_count, "consonants": consonant_count}


print(create_count("Hello World"))
print(create_count("Python"))