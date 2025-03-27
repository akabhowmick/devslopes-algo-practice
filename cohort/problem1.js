/* 
! Maximum Subarray
? Given an integer array nums, find the subarray with the largest sum, and return its sum.
* A subarray is a contiguous non-empty sequence of elements within an array.
! Constraints:
$ 1 <= nums.length <= 105
$ -104 <= nums[i] <= 104
*/

function maxSubArray(nums) {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for(let i = 1; i < nums.length; i++){
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum; 

}

// $ Example 1:
console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])); // * 6
// $ Example 2:
console.log(maxSubArray([1])); // * 1
// $ Example 3:
console.log(maxSubArray([5, 4, -1, 7, 8])); // * 23
// $ Example 4:
console.log(maxSubArray([-5, -4, -1, -7, -8])); // * -1