# Prompt: Write a recursive function that returns the n-th number in the Fibonacci sequence using a recursive approach. 

# version 1 
def fibonacci(n):
   if n <= 0:
       return "Input should be a positive integer"
   elif n == 1:
       return 0
   elif n == 2:
       return 1
   else:
       return fibonacci(n-1) + fibonacci(n-2)
     
     
# Bonus: write a non-recursive, iterative approach.
def fibonacci_iterative(n):
   if n <= 0:
       return "Input should be a positive integer"
   elif n == 1:
       return 0
   elif n == 2:
       return 1
   else:
       a, b = 0, 1
       for _ in range(2, n):
           a, b = b, a + b
       return b
     
# Bonusx2: Memoize this function
def fibonacci_memo(n, memo = {}):
   if n <= 0:
       return "Input should be a positive integer"
   elif n == 1:
       return 0
   elif n == 2:
       return 1
   elif n in memo:
       return memo[n]
   else:
       memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
       return memo[n]
     
#Test (all should return same result)
print(fibonacci(10))
print(fibonacci_iterative(10))
print(fibonacci_memo(10))
print(fibonacci(4))
print(fibonacci_iterative(5))
print(fibonacci_memo(6))
