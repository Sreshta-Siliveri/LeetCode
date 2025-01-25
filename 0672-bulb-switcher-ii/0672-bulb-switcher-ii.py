class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)
        
        # Define possible states based on n and presses
        if presses == 0:
            return 1  # No button pressed, only one state
        if presses == 1:
            return [2, 3, 4][n - 1]  # 2 for n=1, 3 for n=2, 4 for n=3
        if presses == 2:
            return [2, 4, 7][n - 1]  # 2 for n=1, 4 for n=2, 7 for n=3
        
        # For presses >= 3
        return [2, 4, 8][n - 1]  # 2 for n=1, 4 for n=2, 8 for n=3

# Example usage
solution = Solution()

# Example 1
n = 1
presses = 1
print("Output for Example 1:", solution.flipLights(n, presses))  # Output: 2

# Example 2
n = 2
presses = 1
print("Output for Example 2:", solution.flipLights(n, presses))  # Output: 3

# Example 3
n = 3
presses = 1
print("Output for Example 3:", solution.flipLights(n, presses))