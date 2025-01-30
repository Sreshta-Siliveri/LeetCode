class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: If the list is empty or has fewer than 3 elements, no water can be trapped.
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                # If the left bar is smaller, process the left side
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                # If the right bar is smaller or equal, process the right side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped
