class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns
        
        # Step 1: Copy the original matrix into the answer matrix
        answer = [row[:] for row in matrix]
        
        # Step 2: Find the maximum values in each column
        max_in_columns = []
        for j in range(n):
            max_val = float('-inf')
            for i in range(m):
                max_val = max(max_val, matrix[i][j])
            max_in_columns.append(max_val)
        
        # Step 3: Replace -1 with the maximum value in each column
        for i in range(m):
            for j in range(n):
                if answer[i][j] == -1:
                    answer[i][j] = max_in_columns[j]
        
        return answer