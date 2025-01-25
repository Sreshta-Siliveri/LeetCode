class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer k tracks the position for the next unique element
        k = 1
        
        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[i] != nums[i - 1]:
                # Place the unique element in the position marked by k
                nums[k] = nums[i]
                # Move the k pointer forward
                k += 1
        
        # Return the count of unique elements
        return k