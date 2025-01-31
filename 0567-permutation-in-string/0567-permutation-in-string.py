from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, s1 can't be a permutation of any substring of s2
        if len(s1) > len(s2):
            return False
        
        # Initialize counters for s1 and the sliding window
        s1_count = Counter(s1)
        window_count = Counter()
        
        # Initialize the sliding window
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        # Check if the first window is a permutation of s1
        if window_count == s1_count:
            return True
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the character that is moving out of the window
            window_count[s2[i - len(s1)]] -= 1
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            
            # Check if the current window is a permutation of s1
            if window_count == s1_count:
                return True
        
        return False
