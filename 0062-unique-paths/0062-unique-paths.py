class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        # Fill the dp array by calculating the number of paths to each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # The robot can either come from above or left
        
        # The bottom-right corner contains the total number of unique paths
        return dp[m-1][n-1]