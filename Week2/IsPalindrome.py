# Prompt: Write a function that checks if a given string is a palindrome (reads the same forwards and backwards). Ensure the function ignores spaces, punctuation, and case differences when checking for a palindrome.
# Extension: Write a recursive version of this function.


def isPalindrome(str):
    str = str.lower()
    dummy = []
    for i in str:
        if i.isalpha():
            dummy.append(i)
    for i in range(0, len(dummy)):
        if dummy[i] != dummy[len(dummy) - i - 1]:
            return False
    return True


print(isPalindrome("anna21323fasqas"))
print(isPalindrome("RaceCar"))
print(isPalindrome("Race,123,Car"))
