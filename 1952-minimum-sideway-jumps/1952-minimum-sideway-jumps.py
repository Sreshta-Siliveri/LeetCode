from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [1, 0, 1]  # Initial side jumps to reach lanes 1, 2, and 3 at position 0
        
        for i in range(1, n + 1):
            if obstacles[i]:
                dp[obstacles[i] - 1] = float('inf')  # Cannot be in lane with obstacle
            
            min_jumps = min(dp)  # Find the minimum possible jumps at this point
            
            for lane in range(3):
                if obstacles[i] != lane + 1:
                    dp[lane] = min(dp[lane], min_jumps + 1)  # Side jump if needed
                    
        return min(dp)