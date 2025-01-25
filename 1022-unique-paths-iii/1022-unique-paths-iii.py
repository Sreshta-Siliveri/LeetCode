class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_x, start_y = -1, -1
        end_x, end_y = -1, -1
        total_non_obstacles = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # Starting point
                    start_x, start_y = i, j
                elif grid[i][j] == 2:  # Ending point
                    end_x, end_y = i, j
                if grid[i][j] != -1:  # Count non-obstacle cells
                    total_non_obstacles += 1
        
        # Direction vectors for 4-directional movement (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.result = 0  # To store the count of valid paths
        
        # Helper function for DFS
        def dfs(x, y, visited_count):
            if x == end_x and y == end_y:
                if visited_count == total_non_obstacles:
                    self.result += 1
                return
            
            # Temporarily mark the current cell as visited (turn it into an obstacle)
            grid[x][y] = -1  # Mark the cell as visited
            
            # Explore all four directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:  # Valid move
                    dfs(nx, ny, visited_count + 1)
            
            # Backtrack: unmark the current cell
            grid[x][y] = 0
        
        # Start DFS from the starting position
        dfs(start_x, start_y, 1)
        
        return self.result
        