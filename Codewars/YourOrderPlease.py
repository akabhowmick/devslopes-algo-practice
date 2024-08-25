# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
  sentence = sentence.split(' ')
  for i in range(len(sentence)):
    for j in range(len(sentence[i])):
      if sentence[i][j].isdigit():
        sentence[j], sentence[i] = sentence[i], sentence[j]
        
        
  return