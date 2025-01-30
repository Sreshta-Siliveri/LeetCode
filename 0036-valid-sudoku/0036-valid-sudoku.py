class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to keep track of seen values
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]
        
        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                # If the cell is not empty (i.e., not '.'), we need to validate
                if num != '.':
                    # Check if the number is already in the current row, column, or sub-box
                    sub_box_index = (i // 3) * 3 + (j // 3)
                    
                    if num in rows[i]:
                        return False
                    if num in cols[j]:
                        return False
                    if num in sub_boxes[sub_box_index]:
                        return False
                    
                    # Add the number to the corresponding sets
                    rows[i].add(num)
                    cols[j].add(num)
                    sub_boxes[sub_box_index].add(num)
        
        # If no conflicts are found, the Sudoku board is valid
        return True
