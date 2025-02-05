class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = max_zeros = count_ones = count_zeros = 0
        
        for char in s:
            if char == '1':
                count_ones += 1
                count_zeros = 0
            else:
                count_zeros += 1
                count_ones = 0
            
            max_ones = max(max_ones, count_ones)
            max_zeros = max(max_zeros, count_zeros)
        
        return max_ones > max_zeros