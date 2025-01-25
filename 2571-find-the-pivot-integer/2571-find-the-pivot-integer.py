class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        
        # Initialize a variable to store the running sum from 1 to x
        left_sum = 0
        
        # Iterate through numbers from 1 to n to check for pivot
        for x in range(1, n + 1):
            left_sum += x  # Add the current number to the left sum
            # Calculate the right sum using the total sum and the left sum
            right_sum = total_sum - left_sum + x
            # Check if the left sum equals the right sum
            if left_sum == right_sum:
                return x
        
        # Return -1 if no pivot integer is found
        return -1

# Example usage
solution = Solution()

# Example 1
n = 8
print("Output for Example 1:", solution.pivotInteger(n))  # Output: 6

# Example 2
n = 1
print("Output for Example 2:", solution.pivotInteger(n))  # Output: 1

# Example 3
n = 4
print("Output for Example 3:", solution.pivotInteger(n)) 