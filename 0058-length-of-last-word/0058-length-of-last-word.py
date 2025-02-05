class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        # Return the length of the last word
        return len(words[-1])
