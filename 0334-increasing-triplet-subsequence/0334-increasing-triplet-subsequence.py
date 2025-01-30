class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')  # This will hold the smallest number seen so far
        second = float('inf') # This will hold the second smallest number
        
        for num in nums:
            if num <= first:
                first = num  # Update the smallest number
            elif num <= second:
                second = num  # Update the second smallest number
            else:
                # If num > second, we found a valid triplet
                return True
        
        return False
