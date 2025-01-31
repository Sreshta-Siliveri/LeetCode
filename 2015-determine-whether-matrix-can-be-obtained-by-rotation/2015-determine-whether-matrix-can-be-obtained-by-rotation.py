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

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Check if it's possible to rotate mat in 90-degree increments to match target.
        """
        for _ in range(4):  # We check up to 4 rotations (0, 90, 180, 270 degrees)
            if mat == target:
                return True
            self.rotate(mat)  # Rotate mat by 90 degrees clockwise
        return False
