class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find the other two elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

# Example usage
solution = Solution()

# Example 1
nums1 = [-1, 0, 1, 2, -1, -4]
print("Output for Example 1:", solution.threeSum(nums1))

# Example 2
nums2 = [0, 1, 1]
print("Output for Example 2:", solution.threeSum(nums2))

# Example 3
nums3 = [0, 0, 0]
print("Output for Example 3:", solution.threeSum(nums3))

        