from fractions import Fraction
from math import factorial


def expand(x, digits):
    # Convert x to a Fraction to ensure exact arithmetic
    x = Fraction(x).limit_denominator()

    # Initialize the sum of the Taylor series as 1 (first term for e^x is always 1)
    sum_fraction = Fraction(1)

    # term_index tracks the current term in the series expansion, starting from 1 (since x^0 / 0! = 1 is already added)
    term_index = 1

    # power_x keeps track of the power of x, starting with x^0 = 1
    power_x = Fraction(1)

    # Continue adding terms to the series until the numerator of the sum reaches the required number of digits
    while len(str(sum_fraction.numerator)) < digits:
        # Update power_x to the next power of x (x^n)
        power_x *= x

        # Calculate the next term in the series: x^n / n!
        next_term = power_x / factorial(term_index)

        # Add the next term to the running sum of the series
        sum_fraction += next_term

        # Increment the term index for the next iteration
        term_index += 1

    # Return the result as a list [numerator, denominator] of the sum_fraction
    return [sum_fraction.numerator, sum_fraction.denominator]
