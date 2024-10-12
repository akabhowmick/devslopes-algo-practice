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

    roman_numeral = ""

    for value, symbol in val_to_roman:
        while num >= value:
            roman_numeral += symbol
            num -= value

    return roman_numeral


print(intToRoman(3749))  # Output: "MMMDCCXLIX"
print(intToRoman(58))  # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"


# String Concatenation: Instead of appending to a list, directly concatenate the symbols to the roman_numeral string. This maintains the simplicity of the solution while making it more straightforward.

# Time Complexity: Remains O(n) for similar reasons as before.

# Space Complexity: Improved from O(k) due to intermediate storage to O(1) for direct string usage since we're only using one variable for the final output, though concatenating strings in Python can be less efficient than using a list initially due to immutability.