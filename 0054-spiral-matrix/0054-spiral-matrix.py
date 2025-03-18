from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)  # Take the first row
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())  # Take the last column
            if matrix:
                result += matrix.pop()[::-1]  # Take the last row in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))  # Take the first column
        return result
