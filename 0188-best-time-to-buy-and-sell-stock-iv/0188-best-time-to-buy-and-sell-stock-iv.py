from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if n == 0 or k == 0:
            return 0
        
        # If k is greater than or equal to half of the length of the prices array,
        # it's the same as having an infinite number of transactions.
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        
        # dp[i][j] represents the maximum profit on day j with at most i transactions
        dp = [[0] * n for _ in range(k+1)]
        
        # Iterate over each possible transaction count
        for i in range(1, k+1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]
