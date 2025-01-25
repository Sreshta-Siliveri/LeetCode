class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If it's a closing bracket, check if it matches the last opened one
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If stack is empty, all brackets matched properly
        return not stack