class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))

# Example usage
solution = Solution()

# Example 1
n = 3
print("Output for Example 1:", solution.bulbSwitch(n))  # Output: 1

# Example 2
n = 0
print("Output for Example 2:", solution.bulbSwitch(n))  # Output: 0

# Example 3
n = 1
print("Output for Example 3:", solution.bulbSwitch(n)) 