# https://www.codewars.com/kata/58b8d22560873d9068000085/solutions/python
def real_distance(n):
    real_miles = 0
    multiplier = 1

    while n > 0:
        digit = n % 10
        if digit >= 4:  # Adjust for skipped '4'
            digit -= 1

        real_miles += digit * multiplier
        multiplier *= 9
        n //= 10

    return real_miles
