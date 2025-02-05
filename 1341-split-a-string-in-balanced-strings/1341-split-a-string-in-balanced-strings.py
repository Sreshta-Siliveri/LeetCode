class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0  # Counter for balanced substrings
        balance = 0  # Tracks the balance between 'L' and 'R'
        
        for char in s:
            balance += 1 if char == 'R' else -1
            if balance == 0:
                count += 1
        
        return count
