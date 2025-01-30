from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is longer than s, no valid window can exist
        if len(s) < len(t):
            return ""
        
        # Create a counter for the characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Sliding window initialization
        window_count = Counter()
        left = 0
        right = 0
        formed = 0
        min_len = float('inf')
        min_window = ""
        
        # Start sliding window
        while right < len(s):
            # Add character at s[right] to the window
            char = s[right]
            window_count[char] += 1
            
            # Check if the current character's frequency matches the required frequency
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Now try to contract the window if it's valid
            while left <= right and formed == required:
                # Update the result if we found a smaller window
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left:right + 1]
                
                # Try to shrink the window from the left
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                
                left += 1
            
            # Expand the window by moving right pointer
            right += 1
        
        return min_window
