class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0  # Base case: x^0 = 1
        
        if n < 0:
            x = 1 / x  # Handle negative exponent by inverting x
            n = -n
        
        result = 1.0
        while n:
            if n % 2:  # If n is odd, multiply result by x
                result *= x
            x *= x  # Square x
            n //= 2  # Divide n by 2
        
        return result
