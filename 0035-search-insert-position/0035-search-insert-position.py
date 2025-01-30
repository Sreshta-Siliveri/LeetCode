class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Define the left and right pointers
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            
            # If target is found, return its index
            if nums[mid] == target:
                return mid
            # If target is greater, move the left pointer
            elif nums[mid] < target:
                left = mid + 1
            # If target is smaller, move the right pointer
            else:
                right = mid - 1
        
        # If target is not found, return the index where it should be inserted
        return left
