class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0  # Carry for addition
        result = []  # To store the binary result

        # Iterate through both strings from the end
        while i >= 0 or j >= 0 or carry:
            # Get the current digits (convert to integers or use 0 if out of bounds)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum of the current digits and the carry
            total = digit_a + digit_b + carry
            result.append(str(total % 2))  # Append the current binary digit
            carry = total // 2  # Update the carry

            # Move the pointers
            i -= 1
            j -= 1

        # The result is built in reverse order, so reverse it before returning
        return ''.join(result[::-1])

# Example usage
solution = Solution()

# Example 1
a = "11"
b = "1"
print("Output for Example 1:", solution.addBinary(a, b))  # Output: "100"

# Example 2
a = "1010"
b = "1011"
print("Output for Example 2:", solution.addBinary(a, b))