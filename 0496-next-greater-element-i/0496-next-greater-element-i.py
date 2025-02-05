class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        
        # Traverse nums2 to find the next greater element using a stack
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Remaining elements in stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Generate result for nums1 based on the precomputed next greater elements
        return [next_greater[num] for num in nums1]