class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        
        # Initialize the variable to keep track of the maximum area
        max_area = 0
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the current area
            current_area = (right - left) * min(height[left], height[right])
            
            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area