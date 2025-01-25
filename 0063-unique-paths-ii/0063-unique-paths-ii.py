class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the starting point has an obstacle, there are no paths
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Initialize a DP table with all 0s
        dp = [[0] * n for _ in range(m)]
        
        # Set the starting point
        dp[0][0] = 1
        
        # Fill the first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Fill the first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The bottom-right corner contains the answer
        return dp[m-1][n-1]