from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = set()
        
        while queue:
            index = queue.popleft()
            
            if arr[index] == 0:
                return True
            
            visited.add(index)
            
            for next_index in [index + arr[index], index - arr[index]]:
                if 0 <= next_index < n and next_index not in visited:
                    queue.append(next_index)
        
        return False
