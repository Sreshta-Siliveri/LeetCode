class Solution:
    def addOperators(self, num: str, target: int):
        def backtrack(index, prev_operand, current_operand, current_expr):
            # Base case: if we reach the end of the string, check if the expression is valid
            if index == len(num):
                if current_operand == target:
                    result.append(current_expr)
                return

            for i in range(index + 1, len(num) + 1):
                # Extract the current number as a substring
                curr_num_str = num[index:i]
                
                # If the current number has leading zeros, skip it unless it's "0"
                if len(curr_num_str) > 1 and curr_num_str[0] == '0':
                    continue

                curr_num = int(curr_num_str)

                # Recurse with the current number added to the expression
                if index == 0:  # First number, no operator
                    backtrack(i, curr_num, curr_num, curr_num_str)
                else:
                    # Try addition
                    backtrack(i, curr_num, current_operand + curr_num, current_expr + '+' + curr_num_str)
                    # Try subtraction
                    backtrack(i, -curr_num, current_operand - curr_num, current_expr + '-' + curr_num_str)
                    # Try multiplication, handle precedence
                    backtrack(i, prev_operand * curr_num, current_operand - prev_operand + (prev_operand * curr_num), current_expr + '*' + curr_num_str)
                    
        result = []
        backtrack(0, 0, 0, "")
        return result
