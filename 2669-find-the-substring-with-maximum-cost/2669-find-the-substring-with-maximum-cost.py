from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # Create a dictionary to map characters in chars to their respective values in vals
        value_map = {c: v for c, v in zip(chars, vals)}
        
        # Initialize variables for Kadane's algorithm
        current_sum = 0
        max_sum = 0  # We start with 0 because the empty substring has a cost of 0
        
        # Traverse each character in s and calculate the corresponding value
        for char in s:
            # If char is in value_map, use its mapped value, otherwise use its alphabetic position
            if char in value_map:
                value = value_map[char]
            else:
                value = ord(char) - ord('a') + 1
            
            # Apply Kadane's algorithm: update the current sum
            current_sum = max(value, current_sum + value)
            
            # Update the max sum if the current sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum
