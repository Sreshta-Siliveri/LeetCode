from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] != '0':
            return False
        
        queue = deque([0])
        farthest = 0
        
        while queue:
            index = queue.popleft()
            
            start = max(index + minJump, farthest + 1)
            end = min(index + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)
            
            farthest = end
        
        return False
