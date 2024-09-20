// Write a function that takes a list (array) and returns a new list with all duplicate elements removed.
// Extension: Modify the function to maintain the order of the original list.

const removeDuplicates = (listOfNums) => {
  let newList = [];

  for (let i = 0; i < listOfNums.length; i++) {
    // Check if the current element is already in the new list
    if (!newList.includes(listOfNums[i])) {
      newList.push(listOfNums[i]);
    }
  }
  return newList;
}

// Test the function
const inputList = [1, 2, 3, 2, 4, 5, 3, 6, 4, 7];
const result = removeDuplicates(inputList);
console.log(result); // Output: [1, 2, 3, 4, 5, 6, 7]