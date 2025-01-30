class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            # Update `twos` with the bits that appear twice (set them in twos)
            twos |= ones & num
            # Update `ones` with the bits that appear once (set them in ones)
            ones ^= num
            # If a bit appears 3 times, reset both ones and twos for that bit
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        
        return ones
