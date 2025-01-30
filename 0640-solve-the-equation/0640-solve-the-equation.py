class Solution:
    def solveEquation(self, equation: str) -> str:
        # Split equation into left and right sides
        left, right = equation.split('=')
        
        def parse(expression):
            """Parse the expression and return the sum of x-coefficients and numeric constants."""
            coeff, const = 0, 0
            tokens = re.findall(r'[+-]?\d*x?', expression)
            for token in tokens:
                if 'x' in token:
                    if token == 'x' or token == '+x':
                        coeff += 1
                    elif token == '-x':
                        coeff -= 1
                    else:
                        coeff += int(token[:-1])
                elif token:
                    const += int(token)
            return coeff, const
        
        left_coeff, left_const = parse(left)
        right_coeff, right_const = parse(right)
        
        # Simplify equation to ax = b
        coeff_x = left_coeff - right_coeff
        const_b = right_const - left_const
        
        # Check for infinite solutions or no solution
        if coeff_x == 0:
            return "Infinite solutions" if const_b == 0 else "No solution"
        
        # Solve for x
        return f"x={const_b // coeff_x}"
        