class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize variables
        n = len(nums)
        left = 0
        current_sum = 0
        min_len = float('inf')  # Initialize with infinity to find the minimum length
        
        # Traverse through the array with the right pointer
        for right in range(n):
            current_sum += nums[right]
            
            # Try to shrink the window from the left while maintaining the sum >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        # If min_len was updated, return it, otherwise return 0
        return min_len if min_len != float('inf') else 0
