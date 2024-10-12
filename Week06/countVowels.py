def countVowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in str:
        if char.lower() in vowels:
            count += 1
    return count

print(countVowels("Hello World"))  # Output: 3