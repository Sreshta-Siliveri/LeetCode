class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left part is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target in the left sorted part
                else:
                    left = mid + 1  # Target in the right unsorted part
            # If the right part is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target in the right sorted part
                else:
                    right = mid - 1  # Target in the left unsorted part
        
        return -1
