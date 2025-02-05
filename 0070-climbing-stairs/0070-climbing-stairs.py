class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the first two steps
        first, second = 1, 2
        
        for i in range(3, n + 1):
            # The number of ways to reach step i is the sum of the previous two steps
            first, second = second, first + second
        
        return second