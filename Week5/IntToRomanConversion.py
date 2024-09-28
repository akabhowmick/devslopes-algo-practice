def intToRoman(num: int) -> str:
    val_to_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    roman_numeral = []
    
    for value, symbol in val_to_roman:
        while num >= value:
            roman_numeral.append(symbol)
            num -= value
    
    return ''.join(roman_numeral)

print(intToRoman(3749))  #Output: "MMMDCCXLIX"
print(intToRoman(58))    #Output: "LVIII"
print(intToRoman(1994))  #Output: "MCMXCIV"


# Time Complexity: O(n), where n is the integer value being converted. In the worst-case scenario, the while loop iterates n times, especially for smaller values (e.g., 1). However, since the maximum value for a Roman numeral (3999) has a limited number of possible symbols, we can consider it more like O(k) where k is the number of symbols generated. But practically, it's O(n) since the number of symbols generated is proportional to n.

# Space Complexity: O(k), where k is the number of Roman numeral symbols generated, which will be relatively small (at most 15 symbols for the highest value).