from collections import defaultdict

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        pair_sum_count = defaultdict(list)
        quadruplet_count = 0
        
        # Step 1: Store pairs (a, b) with their sums in the dictionary
        for a in range(n - 1):
            for b in range(a + 1, n):
                pair_sum_count[nums[a] + nums[b]].append((a, b))
        
        # Step 2: Iterate over all pairs (c, d) with c < d
        for c in range(2, n):
            for d in range(c + 1, n):
                target_sum = nums[d] - nums[c]
                
                # If target_sum exists in pair_sum_count, check the pairs
                if target_sum in pair_sum_count:
                    # Check for valid (a, b) pairs
                    for a, b in pair_sum_count[target_sum]:
                        if a < b < c:
                            quadruplet_count += 1
        
        return quadruplet_count
