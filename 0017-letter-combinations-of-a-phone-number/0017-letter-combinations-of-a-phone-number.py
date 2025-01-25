class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Map digits to corresponding letters
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        result = []
        
        # Helper function to perform backtracking
        def backtrack(index, current_combination):
            # If we've processed all digits, add the current combination to the result
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the letters corresponding to the current digit
            letters = digit_to_letters[digits[index]]
            
            # For each letter, append it and move to the next digit
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        # Start the backtracking process from index 0 and an empty combination
        backtrack(0, "")
        
        return result