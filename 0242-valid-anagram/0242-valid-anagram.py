from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of s and t are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Count the frequency of characters in both strings
        return Counter(s) == Counter(t)
