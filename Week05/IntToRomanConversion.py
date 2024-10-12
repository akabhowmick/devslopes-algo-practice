def intToRoman(num: int) -> str:
    # Mapping of integer values to their corresponding Roman numeral symbols
    val_to_roman = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    # List to hold the resulting Roman numeral symbols
    roman_numeral = []

    # Iterate over each value-symbol pair in the mapping
    for value, symbol in val_to_roman:
        # While the current number is greater than or equal to the value
        while num >= value:
            # Append the Roman symbol to the result list
            roman_numeral.append(symbol)
            # Subtract the value from the number
            num -= value
    # Join the list of symbols into a single string and return it
    return "".join(roman_numeral)


print(intToRoman(3749))  # Output: "MMMDCCXLIX"
print(intToRoman(58))  # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"


# Time Complexity: O(n), where n is the integer value being converted. In the worst-case scenario, the while loop iterates n times, especially for smaller values (e.g., 1). However, since the maximum value for a Roman numeral (3999) has a limited number of possible symbols, we can consider it more like O(k) where k is the number of symbols generated. But practically, it's O(n) since the number of symbols generated is proportional to n.

# Space Complexity: O(k), where k is the number of Roman numeral symbols generated, which will be relatively small (at most 15 symbols for the highest value).
