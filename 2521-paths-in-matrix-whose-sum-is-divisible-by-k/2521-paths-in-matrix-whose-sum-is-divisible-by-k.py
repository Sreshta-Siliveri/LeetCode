class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # DP table, where dp[i][r] will store the number of paths to (i, j) with remainder r % k
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Initialize the starting point (0, 0)
        dp[0][0][grid[0][0] % k] = 1
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                for remainder in range(k):
                    # Current number at grid[i][j]
                    current = grid[i][j]
                    
                    # If we are not at the first row, propagate values from the top (i-1, j)
                    if i > 0:
                        dp[i][j][(remainder + current) % k] += dp[i-1][j][remainder]
                        dp[i][j][(remainder + current) % k] %= MOD
                    
                    # If we are not at the first column, propagate values from the left (i, j-1)
                    if j > 0:
                        dp[i][j][(remainder + current) % k] += dp[i][j-1][remainder]
                        dp[i][j][(remainder + current) % k] %= MOD
        
        # The answer is the number of paths that reach the bottom-right corner with sum % k == 0
        return dp[m-1][n-1][0]