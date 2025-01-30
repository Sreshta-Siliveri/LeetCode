class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Find the greatest common divisor (GCD) of p and q
        g = math.gcd(p, q)
        
        # Reduce p and q by their GCD
        p //= g
        q //= g
        
        # Check where the laser reaches
        if p % 2 == 0 and q % 2 == 1:
            return 2
        elif p % 2 == 1 and q % 2 == 1:
            return 1
        elif p % 2 == 1 and q % 2 == 0:
            return 0
        else:
            return -1  # This case shouldn't happen for the given constraints.
