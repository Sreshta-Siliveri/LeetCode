class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case
        
        # Compute the minimum coins for each amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If the amount cannot be formed, return -1
        return dp[amount] if dp[amount] != float('inf') else -1