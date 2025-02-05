class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Base cases
        if n == 2:
            return min(cost[0], cost[1])
        
        # Initialize dp array
        dp = [0] * n
        
        # The first two steps
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Fill the dp array
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        # The result is the minimum cost to reach the top
        return min(dp[n-1], dp[n-2])