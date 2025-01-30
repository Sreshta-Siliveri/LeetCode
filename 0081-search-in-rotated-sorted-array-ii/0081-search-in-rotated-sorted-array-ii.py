class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if the target is at the middle
            if nums[mid] == target:
                return True
            
            # Handle duplicates: If left, mid, and right are the same, we can't decide which half is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # If the left half is sorted
            elif nums[left] <= nums[mid]:
                # Check if target lies in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search in the left half
                else:
                    left = mid + 1  # Search in the right half
            # If the right half is sorted
            else:
                # Check if target lies in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Search in the right half
                else:
                    right = mid - 1  # Search in the left half
        
        return False
