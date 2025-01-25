class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = k
        
        # Iterate from the end of the num array
        while i >= 0:
            carry += num[i]  # Add the carry to the current digit
            num[i] = carry % 10  # Update the digit
            carry //= 10  # Update the carry
            i -= 1  # Move to the previous digit
        
        # If carry is left after processing all digits, handle it
        while carry > 0:
            num.insert(0, carry % 10)
            carry //= 10
        
        return num

# Example usage
solution = Solution()

# Example 1
num = [1, 2, 0, 0]
k = 34
print("Output for Example 1:", solution.addToArrayForm(num, k))  # Output: [1, 2, 3, 4]

# Example 2
num = [2, 7, 4]
k = 181
print("Output for Example 2:", solution.addToArrayForm(num, k))  # Output: [4, 5, 5]

# Example 3
num = [2, 1, 5]
k = 806
print("Output for Example 3:", solution.addToArrayForm(num, k))