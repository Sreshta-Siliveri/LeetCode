from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()  # Sort processor times in ascending order
        tasks.sort(reverse=True)  # Sort task times in descending order
        
        max_time = 0
        n = len(processorTime)
        
        for i in range(n):
            # Assign the 4 largest remaining tasks to the current processor
            max_time = max(max_time, processorTime[i] + tasks[i * 4])
        
        return max_time
