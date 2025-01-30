class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # Initialize dp array with 0s
        dp = [0] * (n + 1)
        max_length = 0
        
        # Iterate through nums1 and nums2
        for i in range(1, m + 1):
            # We need to iterate backwards through nums2 to avoid overwriting dp values in the same row
            for j in range(n, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    max_length = max(max_length, dp[j])
                else:
                    dp[j] = 0
        
        return max_length
