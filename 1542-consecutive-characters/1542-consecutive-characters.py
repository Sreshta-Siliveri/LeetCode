class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1  # Minimum length of a non-empty substring is 1
        current_power = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_power += 1
            else:
                max_power = max(max_power, current_power)
                current_power = 1
        
        # At the end, we need to check the last sequence
        max_power = max(max_power, current_power)
        
        return max_power
        