from typing import List

class Solution:
    def is_subsequence(self, s1: str, s2: str) -> bool:
        """Check if s1 is a subsequence of s2"""
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1)
    
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)  # Sort strings by length in descending order
        
        for i, s in enumerate(strs):
            is_uncommon = True
            for j, t in enumerate(strs):
                if i != j and self.is_subsequence(s, t):  
                    is_uncommon = False
                    break
            if is_uncommon:
                return len(s)  # Return the length of the longest uncommon subsequence
        
        return -1  # If no LUS found
