import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # sub will store the smallest tail of all increasing subsequences of length i+1
        sub = []
        
        for num in nums:
            # Find the position to replace in the sub array
            pos = bisect.bisect_left(sub, num)
            # If pos is equal to the length of sub, it means num is larger than any element in sub
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        
        # The length of sub will give the length of the longest increasing subsequence
        return len(sub)
