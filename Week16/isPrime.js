// Prompt: Write a function that determines if a number is prime. 
// Extension: Modify the function to return an array of all prime numbers less than the given number."

function isPrime(number) {
  if (number <= 1) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      return false;
    }
  }

  return true;
}

// Example Usage:
console.log(isPrime(17)); // Output: true
console.log(isPrime(18)); // Output: false

function findPrimesLessThan(limit) {
  const primes = [];

  for (let i = 2; i < limit; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }

  return primes;
}

// Example usage:
console.log(findPrimesLessThan(20)); // Output: [2, 3, 5, 7, 11, 13, 17, 19]
console.log(findPrimesLessThan(50)); // Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]