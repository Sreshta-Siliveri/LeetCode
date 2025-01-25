class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                # If current element is not val, place it at position k
                nums[k] = nums[i]
                # Move the k pointer forward
                k += 1
        
        # Return the count of valid elements
        return k