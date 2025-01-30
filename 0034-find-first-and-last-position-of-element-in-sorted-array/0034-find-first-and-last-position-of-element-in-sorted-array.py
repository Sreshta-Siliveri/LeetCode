class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        # Find the left boundary (first occurrence)
        left_index = binary_search_left(nums, target)
        # If target is not in the array, return [-1, -1]
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        
        # Find the right boundary (last occurrence)
        right_index = binary_search_right(nums, target)
        
        return [left_index, right_index]
