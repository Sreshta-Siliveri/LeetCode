from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix in-place by 90 degrees clockwise.
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
