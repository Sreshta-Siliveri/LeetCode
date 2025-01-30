class Solution:
    def calculate(self, s: str) -> int:
        # Stack to store the numbers and intermediate results
        stack = []
        # The current number being processed
        current_number = 0
        # The last operator encountered
        last_operator = "+"
        
        # Iterate through the string
        for i, char in enumerate(s):
            # If the character is a digit, build the current number
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # If the character is an operator or we reach the end of the string
            if char in "+-*/" or i == len(s) - 1:
                if last_operator == "+":
                    stack.append(current_number)
                elif last_operator == "-":
                    stack.append(-current_number)
                elif last_operator == "*":
                    stack[-1] = stack[-1] * current_number
                elif last_operator == "/":
                    # Handle truncation towards zero
                    if stack[-1] // current_number < 0 and stack[-1] % current_number != 0:
                        stack[-1] = stack[-1] // current_number + 1
                    else:
                        stack[-1] = stack[-1] // current_number
                
                # Reset current number and update the operator
                current_number = 0
                last_operator = char
        
        # The result is the sum of the numbers in the stack
        return sum(stack)
