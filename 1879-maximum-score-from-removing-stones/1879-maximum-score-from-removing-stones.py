class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # Sort the three piles in ascending order
        x, y, z = sorted([a, b, c])
        
        # If the sum of the two smaller piles is less than or equal to the largest pile,
        # we can only take stones from them until they are empty
        if x + y <= z:
            return x + y
        
        # Otherwise, we can pair off stones optimally
        return (x + y + z) // 2
