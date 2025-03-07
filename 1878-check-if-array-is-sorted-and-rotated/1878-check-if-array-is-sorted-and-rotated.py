from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count_breaks = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check if there's a break in sorting
                count_breaks += 1
            
            if count_breaks > 1:  # More than one break means it's not a rotated sorted array
                return False
        
        return True
