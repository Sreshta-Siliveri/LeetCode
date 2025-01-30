class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define the integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge case of overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        # Using bitwise subtraction method
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        # Apply the sign
        quotient = -quotient if negative else quotient
        
        return max(min(quotient, INT_MAX), INT_MIN)
