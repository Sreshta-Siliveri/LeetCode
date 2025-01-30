import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        # Iterate over all pairs (a, b)
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # Calculate a^2 + b^2
                sum_of_squares = a * a + b * b
                # Find the square root of the sum
                c = int(math.isqrt(sum_of_squares))
                
                # Check if c^2 is equal to the sum_of_squares and c is within the range
                if c * c == sum_of_squares and c <= n:
                    count += 1
        
        return count
