from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = max_val = curr = 0
        
        # Compute the running sum to reconstruct possible hidden sequences
        for diff in differences:
            curr += diff
            min_val = min(min_val, curr)  # Track the lowest possible value
            max_val = max(max_val, curr)  # Track the highest possible value

        # The range of valid starting values
        min_start = lower - min_val
        max_start = upper - max_val

        # The number of valid starting values
        return max(0, max_start - min_start + 1)
