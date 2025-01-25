class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize with -1 to handle the case of valid substring from the start
        max_len = 0  # Variable to track the maximum length of valid parentheses
        
        # Traverse the string
        for i, char in enumerate(s):
            if char == '(':  # If it's an opening parenthesis, push its index onto the stack
                stack.append(i)
            else:  # If it's a closing parenthesis
                stack.pop()  # Pop the last opening parenthesis index
                if stack:
                    # Calculate the length of the valid substring
                    max_len = max(max_len, i - stack[-1])
                else:
                    # If the stack is empty, push the current index as the new base
                    stack.append(i)
        
        return max_len