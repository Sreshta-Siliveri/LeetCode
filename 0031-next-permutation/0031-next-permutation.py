class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the largest index i such that nums[i] < nums[i + 1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If i is not negative, there is a next permutation
        if i >= 0:
            # Step 2: Find the largest index j such that nums[j] > nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray from i + 1 to the end
        nums[i + 1:] = reversed(nums[i + 1:])
