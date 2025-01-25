class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits of the absolute value
        reversed_x = int(str(x)[::-1])
        
        # Restore the sign and check for overflow
        reversed_x *= sign
        
        # Check if the reversed number is within the 32-bit signed integer range
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x