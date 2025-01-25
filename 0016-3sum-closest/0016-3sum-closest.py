class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # Initialize the closest sum with a very large value
        closest_sum = float('inf')
        
        # Iterate through the array
        for i in range(len(nums) - 2):
            # Use two pointers to find the other two elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on the comparison with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the current_sum equals the target, return it immediately
                    return current_sum
        
        return closest_sum

# Example usage
solution = Solution()

# Example 1
nums1 = [-1, 2, 1, -4]
target1 = 1
print("Output for Example 1:", solution.threeSumClosest(nums1, target1))

# Example 2
nums2 = [0, 0, 0]
target2 = 1
print("Output for Example 2:", solution.threeSumClosest(nums2, target2))