from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current_sum with the first element, and max_sum as the first element
        current_sum = max_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Calculate the new current sum
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the maximum sum found so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum
