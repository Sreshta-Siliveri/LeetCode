class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array to store the intermediate sums
        result = [0] * (len(num1) + len(num2))
        
        # Reverse the strings for easier calculation
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Multiply each digit of num1 with each digit of num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit_product = int(num1[i]) * int(num2[j])
                # Add the product to the current position in the result array
                result[i + j] += digit_product
                # Carry over if the value at the position is >= 10
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Remove leading zeros from the result array
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert result array back to a string and reverse it
        return ''.join(map(str, result[::-1]))

# Example usage
solution = Solution()

# Example 1
num1 = "2"
num2 = "3"
print("Output for Example 1:", solution.multiply(num1, num2))  # Output: "6"

# Example 2
num1 = "123"
num2 = "456"
print("Output for Example 2:", solution.multiply(num1, num2))