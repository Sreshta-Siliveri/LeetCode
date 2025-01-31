from typing import List
from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:  # First jump must be exactly 1
            return False

        stone_set = set(stones)
        target = stones[-1]
        
        @lru_cache(None)
        def dfs(position: int, jump: int) -> bool:
            if position == target:
                return True
            
            if position not in stone_set or jump <= 0:
                return False
            
            for next_jump in (jump - 1, jump, jump + 1):
                if next_jump > 0 and (position + next_jump) in stone_set:
                    if dfs(position + next_jump, next_jump):
                        return True
            
            return False
        
        return dfs(1, 1)  # Start from stone at position 1 with a jump size of 1
