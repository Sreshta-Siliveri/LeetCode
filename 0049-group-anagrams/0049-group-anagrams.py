from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store groups of anagrams
        anagram_map = {}
        
        # Iterate through each string in the input list
        for word in strs:
            # Sort the word and use the sorted word as a key
            sorted_word = ''.join(sorted(word))
            
            # If the key is not in the dictionary, add it
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            
            # Append the original word to the corresponding group
            anagram_map[sorted_word].append(word)
        
        # Return the grouped anagrams as a list of lists
        return list(anagram_map.values())
