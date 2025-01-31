from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            # If we've reached the end, add the current permutation to the result
            if start == len(nums):
                result.append(nums[:])  # Append a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                # Swap the current index with the start
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next index
                backtrack(start + 1)
                # Swap back to undo the change and explore other possibilities
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0)  # Start the backtracking from the first index
        return result
