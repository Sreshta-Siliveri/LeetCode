class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, current_combination):
            # If the target becomes 0, it means we found a valid combination
            if target == 0:
                result.append(list(current_combination))
                return
            
            # Iterate over the candidates starting from 'start' index to avoid duplicates
            for i in range(start, len(candidates)):
                # If the candidate is greater than the target, no point in exploring further
                if candidates[i] > target:
                    continue
                
                # Choose the current candidate and explore further
                current_combination.append(candidates[i])
                # The next recursive call should start from the same 'i' to allow repeated use of candidates
                backtrack(i, target - candidates[i], current_combination)
                # Backtrack by removing the last chosen element
                current_combination.pop()
        
        # Start the backtracking from the first candidate
        backtrack(0, target, [])
        
        return result
