from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the children's greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child_idx, cookie_idx = 0, 0
        content_children = 0
        
        # Use two pointers to match children with cookies
        while child_idx < len(g) and cookie_idx < len(s):
            if s[cookie_idx] >= g[child_idx]:
                # If the current cookie can satisfy the current child, increment content children
                content_children += 1
                child_idx += 1  # Move to the next child
            # Always move to the next cookie
            cookie_idx += 1
        
        return content_children
