class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        power = 2 ** k
        
        # Step 1: Compute prefix and suffix ORs
        prefix_or = [0] * n
        suffix_or = [0] * n
        
        prefix_or[0] = nums[0]
        for i in range(1, n):
            prefix_or[i] = prefix_or[i - 1] | nums[i]
        
        suffix_or[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_or[i] = suffix_or[i + 1] | nums[i]
        
        # Step 2: Calculate maximum OR
        max_or = 0
        for i in range(n):
            # Compute OR without nums[i]
            left_or = prefix_or[i - 1] if i > 0 else 0
            right_or = suffix_or[i + 1] if i < n - 1 else 0
            
            # Multiply nums[i] by 2^k
            new_or = (nums[i] * power) | left_or | right_or
            max_or = max(max_or, new_or)
        
        return max_or