class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Rearrange the array such that every number nums[i] should be at position nums[i] - 1
        for i in range(n):
            # Keep swapping nums[i] to its correct position as long as the number is in the range [1, n]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap the current element with the element at its target index (nums[i] - 1)
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first position where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all positions are correct, the missing number is n + 1
        return n + 1
