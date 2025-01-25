class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = Counter()
            left = 0
            result = 0
            for right in range(len(nums)):
                # Add the current element to the window
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1
                
                # Shrink the window if there are more than k distinct elements
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                
                # Add the number of valid subarrays ending at `right`
                result += right - left + 1
            
            return result
        
        # Number of subarrays with exactly k distinct integers
        return atMost(k) - atMost(k - 1)