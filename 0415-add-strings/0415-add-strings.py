class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0  # To keep track of carry
        result = []  # To store the result as a list of characters
        
        # Loop until we process all digits in both strings or there is a carry
        while i >= 0 or j >= 0 or carry:
            # Get the current digit from num1 or 0 if out of bounds
            digit1 = int(num1[i]) if i >= 0 else 0
            # Get the current digit from num2 or 0 if out of bounds
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Calculate the sum of digits and the carry
            current_sum = digit1 + digit2 + carry
            carry = current_sum // 10  # Update carry for the next step
            result.append(str(current_sum % 10))  # Append the last digit of the sum
            
            # Move the pointers to the next digits
            i -= 1
            j -= 1
        
        # The result list contains digits in reverse order, so reverse and join them
        return ''.join(result[::-1])

# Example usage
solution = Solution()

# Example 1
num1 = "11"
num2 = "123"
print("Output for Example 1:", solution.addStrings(num1, num2))  # Output: "134"

# Example 2
num1 = "456"
num2 = "77"
print("Output for Example 2:", solution.addStrings(num1, num2))  # Output: "533"

# Example 3
num1 = "0"
num2 = "0"
print("Output for Example 3:", solution.addStrings(num1, num2))