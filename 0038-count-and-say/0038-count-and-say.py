class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        
        for _ in range(n - 1):
            current = result
            result = ""
            count = 1  # Start counting the first character
            
            # Iterate through the current string
            for i in range(1, len(current)):
                if current[i] == current[i - 1]:  # Same character
                    count += 1
                else:  # Different character, process the previous run
                    result += str(count) + current[i - 1]
                    count = 1  # Reset count
            
            # Add the last group
            result += str(count) + current[-1]
        
        return result