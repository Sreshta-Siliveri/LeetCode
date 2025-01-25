class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string and distribute characters in zigzag pattern
        for char in s:
            rows[current_row] += char
            
            # Determine whether to move up or down the rows
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down  # Switch direction
            
            # Move to the next row in the current direction
            current_row += 1 if going_down else -1
        
        # Join all rows to form the final string
        return ''.join(rows)