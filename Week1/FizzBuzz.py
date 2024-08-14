# Write a function that prints numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".


def fizzBuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:  # Check if number is divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Check if number is divisible by 3
            print("Fizz")
        elif i % 5 == 0:  # Check if number is divisible by 5
            print("Buzz")
        else:  # Print the number itself
            print(i)


fizzBuzz()
