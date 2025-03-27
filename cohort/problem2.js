/* 
$ Coins for Change

? You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
? Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
? You may assume that you have an infinite number of each kind of coin.

! Constraints:

$ 1 <= coins.length <= 12
$ 1 <= coins[i] <= 2^31 - 1
$ 0 <= amount <= 10^4

*/

function coinChange(coins, amount) {
  // better to fill it as amount + 1 
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0; 

  for(let coin of coins){
    for(let i = coin; i <= amount; i++){
      dp[i] = Math.min(dp[i], dp[i - coin] + 1); 
    }
  }

  return dp[amount] === Infinity ? -1 : dp[amount]; 

}

// $ Example 1
console.log(coinChange([1, 2, 5], 11)); // $ Output => 3
// $ Example 2
console.log(coinChange([2], 3)); // $  Output => -1
// $ Example 3
console.log(coinChange([1], 0)); // $ Output => 0
// $ Example 4
console.log(coinChange([1, 6, 7, 9, 11], 13)); // $ Output => 2