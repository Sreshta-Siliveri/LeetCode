from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Edge case: If s or words are empty, return an empty list
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)  # Create a word frequency map
        
        result = []
        
        # Slide the window across the string s, considering all possible starting points
        for i in range(word_len):  # We need to check every possible starting point within one word length
            left = i
            right = i
            window_map = Counter()
            
            while right + word_len <= len(s):
                # Extract the word at the right side of the window
                word = s[right:right + word_len]
                right += word_len
                
                # If the word is part of words, process it
                if word in word_map:
                    window_map[word] += 1
                    
                    # If we have more of this word than needed, move the left pointer to reduce count
                    while window_map[word] > word_map[word]:
                        window_map[s[left:left + word_len]] -= 1
                        left += word_len
                    
                    # If the current window is valid, add the starting index to the result
                    if right - left == total_len:
                        result.append(left)
                else:
                    # If the word is not in words, reset the window
                    left = right
                    window_map.clear()
        
        return result
