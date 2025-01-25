class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the current digit is less than 9, increment it and return the result
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0
            digits[i] = 0
        
        # If we exit the loop, it means all the digits were 9
        # Add a leading 1 to the result
        return [1] + digits

# Example usage
solution = Solution()

# Example 1
digits = [1, 2, 3]
print("Output for Example 1:", solution.plusOne(digits))  # Output: [1, 2, 4]

# Example 2
digits = [4, 3, 2, 1]
print("Output for Example 2:", solution.plusOne(digits))  # Output: [4, 3, 2, 2]

# Example 3
digits = [9]
print("Output for Example 3:", solution.plusOne(digits))