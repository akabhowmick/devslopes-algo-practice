solved = "Exponentials as fractions - 8; Matrix Determinant - 8; Convert string to camel case - 3; String ends with? - 2; Simple Maths Test - 2; Recover a secret string from random triplets - 8; First non-repeating character - 5; Sum of two lowest positive integers - 2; Geometry Basics: Circle Area in 2D - 1; Moving Zeros To The End - 5; Vowel Count - 2; Is a number prime? - 3; Simple Fun #178: Faulty Odometer - 5; Find the divisors! - 2; Does my number look big in this? - 3; Stringing+Me+Along - 3; Is It Even - 1; Are they the same? - 3; Sum of pairs - 5; Greed is good  - 5; Pyramid slide down - 8; RGB - HEX - 5; Molecules to atoms - 5; Reversed Strings - 1; Convert boolean values to strings 'Yes' or 'No' - 1; Disemvowel Trolls - 2; Common Denominators - 5; You're a square! - 2; Nesting Structure Comparison - 8; Sum Strings as Numbers - 8; Codewars style ranking system - 8; Simplifying multilinear polynomials - 8; Next smaller number with the same digits - 8; Path Finder #2: shortest path - 8; Duplicate Encoder - 3; Isograms - 2; Counting Duplicates - 3; Is this a triangle? - 2; Catching Car Mileage Numbers - 8; Path Finder #1: can you reach the exit? - 8; Convert a String to a Number! - 1; Human Readable Time - 5; Binary Addition - 2; Persistent Bugger - 3; Calculating with Functions - 5; Get the Middle Character - 2; Sort the odd - 3; Find the missing letter - 3; Roman Numerals Encoder - 3; Primes in numbers - 5; Find The Parity Outlier - 3; Find the unique number - 3; Maximum subarray sum - 5; Weight for weight - 5; Build Tower - 3; Range Extraction - 8; Snail - 8; Can you get the loop ? - 5; Shortest Knight Path - 8; Square into Squares. Protect trees! - 8; Last digit of a large number - 5; Adding Big Numbers - 8; Find the next perfect square! - 2; Differentiate a polynomial - 8; Twice linear - 8; Connect Four - 8; Replace With Alphabet Position - 3; Boggle Word Checker - 8; Regex validate PIN code - 2; Sum of positive - 1; Century From Year - 1; Square(n) Sum - 1; Who likes it? - 3; So Many Permutations! - 8; Sort binary tree by levels - 8; On the clock - 3; Text align justify - 8; Simple Prime Number Generator - 2"


def parse_string(string):
    tasks = string.split("; ")
    total_sum = 0

    for task in tasks:
        task_parts = task.rsplit(
            " - ", 1
        )  
        try:
            total_sum += int(
                task_parts[1]
            )  
        except ValueError:
            print(
                f"Error converting {task_parts[1]} to integer in task: {task_parts[0]}"
            )

    print(total_sum)
    return total_sum


parse_string(solved)
