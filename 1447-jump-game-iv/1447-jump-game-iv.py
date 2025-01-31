from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)
        
        queue = deque([0])
        visited = set([0])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                
                if i == n - 1:
                    return steps
                
                for j in graph[arr[i]]:
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)
                
                graph[arr[i]].clear()
                
                for j in [i - 1, i + 1]:
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        queue.append(j)
            
            steps += 1
        
        return -1
