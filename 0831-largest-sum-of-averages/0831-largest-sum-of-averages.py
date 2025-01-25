class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        # Calculate prefix sums
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # dp[i][j] represents the maximum score for first i elements with j subarrays
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base case: one subarray
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i
        
        # Fill the dp table
        for j in range(2, k + 1):  # Number of subarrays
            for i in range(1, n + 1):  # Consider first i elements
                for p in range(j - 1, i):  # Last subarray starts from p+1
                    dp[i][j] = max(dp[i][j], dp[p][j - 1] + (prefix[i] - prefix[p]) / (i - p))
        
        return dp[n][k]