# Write a function that takes a string as input and returns the string reversed

def reverse_string(input_string):
    reversed_string = ""
    for i in range(len(input_string)):
        reversed_string += input_string[len(input_string) - 1 - i]
    return reversed_string
  

# using python's index methods using slicing   
def reverse_string(input_string):
    return input_string[::-1]

