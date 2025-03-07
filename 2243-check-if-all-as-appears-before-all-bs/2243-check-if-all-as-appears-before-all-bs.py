class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s  # If "ba" appears, then an 'a' comes after a 'b', so return False
