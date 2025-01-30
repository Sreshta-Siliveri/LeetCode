class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split("+")
        min_value = float('inf')
        best_expr = ""
        
        # Iterate through possible placements of parentheses
        for i in range(len(num1)):
            left_part = num1[:i] or "1"  # Avoid empty string by treating as 1
            mid_left = num1[i:]
            
            for j in range(1, len(num2) + 1):
                mid_right = num2[:j]
                right_part = num2[j:] or "1"  # Avoid empty string by treating as 1
                
                # Compute expression value
                current_value = int(left_part) * (int(mid_left) + int(mid_right)) * int(right_part)
                
                # Update minimum value and expression
                if current_value < min_value:
                    min_value = current_value
                    best_expr = f"{num1[:i]}({num1[i:]}+{num2[:j]}){num2[j:]}"
                    
        return best_expr
