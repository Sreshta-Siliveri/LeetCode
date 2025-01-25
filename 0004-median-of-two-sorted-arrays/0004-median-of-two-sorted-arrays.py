class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        
        # Binary search on the smaller array
        left, right = 0, m
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Edge cases for partitioning at boundaries
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if the partition is valid
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd length combined array
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # Even length combined array
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                # Move towards the left in nums1
                right = partition1 - 1
            else:
                # Move towards the right in nums1
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted.")