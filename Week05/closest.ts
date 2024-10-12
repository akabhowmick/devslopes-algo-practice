// You are given an array of integers, nums, and another integer, target. Your task is to identify three distinct elements from the array such that their combined sum is as close as possible to the value of target.

// Your solution should return this closest possible sum of the three elements.

// You can assume there is always exactly one unique combination that results in the closest sum.

export function closest(nums: number[], target: number): number {
  // Step 1: Sort the array O(log(n))
  nums.sort((a, b) => a - b);

  let closestSum = Infinity; // Start with an infinitely large value for closest sum

  // Step 2: Iterate through the array
  for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1;
    let right = nums.length - 1;

    // Step 3: Two-pointer technique to find the best sum for this i
    while (left < right) {
      const currentSum = nums[i] + nums[left] + nums[right];

      // Step 4: Check if this sum is closer to the target
      if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
        closestSum = currentSum; // Update closest sum
      }

      // Step 5: Adjust pointers based on the sum
      if (currentSum < target) {
        left++; // Increase left pointer to get a larger sum
      } else if (currentSum > target) {
        right--; // Decrease right pointer to get a smaller sum
      } else {
        // If the sum is exactly equal to the target, we return immediately
        return currentSum;
      }
    }
  }

  return closestSum;
}

module.exports = { closest };
