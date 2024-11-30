// Prompt: Given an array of integers, find the highest product of two unique numbers in the array.

const highestProduct = (arr) => {
  if (arr.length < 2) {
    throw new Error("Array must contain at least two numbers.");
  }

  arr.sort((a, b) => a - b);

  const n = arr.length;
  const product1 = arr[n - 1] * arr[n - 2];

  const product2 = arr[0] * arr[1];

  return Math.max(product1, product2);
};

// Test cases
console.log(highestProduct([1, 2, 3, 4, 5]));
console.log(highestProduct([1, 2, 5, 4, 5]));
console.log(highestProduct([-1, 2, 3, 4, 5]));
console.log(highestProduct([-1, 2, -3, 4, 5]));
console.log(highestProduct([1, 2, -3, -4, 5]));
console.log(highestProduct([-1, 2, -3, -4, -5]));
