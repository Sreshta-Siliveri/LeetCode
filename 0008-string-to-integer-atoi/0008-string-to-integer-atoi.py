class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Initialize the sign and index for digit reading
        sign = 1
        index = 0
        
        # Check for the sign at the beginning
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        
        # Initialize result to 0
        result = 0
        
        # Read digits and build the result
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        # Apply sign to the result
        result *= sign
        
        # Handle overflow for 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        
        return result