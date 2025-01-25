class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current, open_count, close_count):
            # Base case: if the length of current string is 2 * n, add it to the result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # If we can add an opening parenthesis, do it
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # If we can add a closing parenthesis, do it
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # Start backtracking with an empty string, 0 opening and 0 closing parentheses
        backtrack("", 0, 0)
        
        return result