class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # Sort the candidates to easily skip duplicates
        candidates.sort()
        
        def backtrack(start, target, current_combination):
            # If the remaining target is zero, we've found a valid combination
            if target == 0:
                result.append(list(current_combination))
                return
            
            # Iterate through the candidates starting from 'start' index
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If the current candidate is greater than the target, no need to continue
                if candidates[i] > target:
                    break
                
                # Include the current number and recurse with the updated target
                current_combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current_combination)
                # Backtrack: remove the last element and try the next possibility
                current_combination.pop()
        
        # Start backtracking
        backtrack(0, target, [])
        
        return result
