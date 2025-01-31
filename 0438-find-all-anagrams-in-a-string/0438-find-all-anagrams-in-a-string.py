from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialize the result list and counters for p and the sliding window
        result = []
        p_count = Counter(p)  # Frequency count of characters in p
        window_count = Counter()  # Frequency count of characters in the current window of s
        
        # Lengths of s and p
        len_s, len_p = len(s), len(p)
        
        # Edge case: if p is longer than s, return an empty list
        if len_s < len_p:
            return result
        
        # Loop through string s
        for i in range(len_s):
            # Add the current character to the sliding window count
            window_count[s[i]] += 1
            
            # Remove the character left behind if the window size exceeds len(p)
            if i >= len_p:
                if window_count[s[i - len_p]] == 1:
                    del window_count[s[i - len_p]]  # Remove it from the window count
                else:
                    window_count[s[i - len_p]] -= 1  # Decrease its count
            
            # Compare the counts of the current window with p's counts
            if window_count == p_count:
                result.append(i - len_p + 1)  # Add the starting index of the window
        
        return result
