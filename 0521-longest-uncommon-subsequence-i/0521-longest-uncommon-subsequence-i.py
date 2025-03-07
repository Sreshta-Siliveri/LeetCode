class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1  # No uncommon subsequence if both strings are identical
        return max(len(a), len(b))