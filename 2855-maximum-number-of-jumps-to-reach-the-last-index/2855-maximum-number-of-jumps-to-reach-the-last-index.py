from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n  # Initialize DP array with -1 (unreachable states)
        dp[0] = 0  # Start at index 0 with 0 jumps
        
        for i in range(n):
            if dp[i] == -1:
                continue  # Skip unreachable indices
            
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:  # Check valid jump condition
                    dp[j] = max(dp[j], dp[i] + 1)  # Update DP table with max jumps
        
        return dp[-1]
