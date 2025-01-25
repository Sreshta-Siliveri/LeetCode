class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # To store characters in the current window
        left = 0  # Left pointer for the sliding window
        max_length = 0  # Maximum length of substring without repeating characters

        for right in range(len(s)):
            # If the character at `right` is already in the window, shrink the window
            while s[right] in seen:
                seen.remove(s[left])  # Remove the character at `left` from the set
                left += 1  # Move the left pointer forward
            
            # Add the current character to the set and update max length
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length