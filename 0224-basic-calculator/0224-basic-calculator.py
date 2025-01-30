class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build multi-digit number
            elif char in ['+', '-']:
                result += sign * num  # Apply previous number
                num = 0  # Reset number
                sign = 1 if char == '+' else -1  # Update sign
            elif char == '(':
                stack.append(result)  # Store previous result
                stack.append(sign)  # Store previous sign
                result = 0  # Reset result inside parentheses
                sign = 1  # Reset sign inside parentheses
            elif char == ')':
                result += sign * num  # Apply last number before closing bracket
                num = 0  # Reset number
                result *= stack.pop()  # Multiply by sign before '('
                result += stack.pop()  # Add result before '('
        
        return result + (sign * num)  # Add any remaining number
