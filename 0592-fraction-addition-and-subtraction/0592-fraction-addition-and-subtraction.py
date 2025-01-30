from fractions import Fraction
import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Find all fractions in the expression
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        # Convert fractions to Fraction objects and sum them
        result = sum(Fraction(frac) for frac in fractions)

        # Return the result in irreducible fraction format
        return f"{result.numerator}/{result.denominator}"