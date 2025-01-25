class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = defaultdict(int)
        count = 0
        
        # Step 1: Calculate sums of all pairs from nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum_map[num1 + num2] += 1
        
        # Step 2: Check sums of all pairs from nums3 and nums4 and find matches in sum_map
        for num3 in nums3:
            for num4 in nums4:
                count += sum_map[-(num3 + num4)]
        
        return count