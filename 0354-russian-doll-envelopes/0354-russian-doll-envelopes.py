import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width in ascending order and by height in descending order if widths are equal
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract heights after sorting
        heights = [h for _, h in envelopes]
        
        # Now, apply LIS on the heights using binary search
        # We will use a list to maintain the potential ends of increasing subsequences
        lis = []
        
        for h in heights:
            # Find the position to replace in the lis list
            pos = bisect.bisect_left(lis, h)
            # If pos is equal to the length of lis, it means h is larger than any element in lis
            if pos == len(lis):
                lis.append(h)
            else:
                lis[pos] = h
        
        # The length of lis will give the maximum number of envelopes we can Russian doll
        return len(lis)
