class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flip = 0
        count = 0

        for i, flip in enumerate(flips, start=1):  # i is 1-indexed
            max_flip = max(max_flip, flip)
            if max_flip == i:
                count += 1

        return count