class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True  # 0 and 1 are perfect squares
        
        left, right = 1, num // 2
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False