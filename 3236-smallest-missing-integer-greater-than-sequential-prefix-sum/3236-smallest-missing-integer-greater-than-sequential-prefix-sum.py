class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        # Find the smallest missing integer >= seq_sum
        while seq_sum in nums:
            seq_sum += 1
        
        return seq_sum