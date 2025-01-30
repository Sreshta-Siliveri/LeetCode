class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate the sum of integers from 0 to n
        n = len(nums)
        sum_n = n * (n + 1) // 2
        
        # Calculate the sum of the numbers in the array
        sum_nums = sum(nums)
        
        # The missing number is the difference between the two sums
        return sum_n - sum_nums
