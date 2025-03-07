class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, 
                     x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point (px, py) on the rectangle to the circle's center
        px = min(max(xCenter, x1), x2)
        py = min(max(yCenter, y1), y2)
        
        # Compute the squared distance from the closest point to the circle's center
        distance_squared = (px - xCenter) ** 2 + (py - yCenter) ** 2
        
        # Check if the squared distance is within the squared radius
        return distance_squared <= radius ** 2
