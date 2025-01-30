class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all elements to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find the rightmost set bit (this is the bit that is different between the two unique numbers)
        rightmost_set_bit = xor_all & -xor_all
        
        # Step 3: Partition the numbers into two groups and XOR them separately
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
