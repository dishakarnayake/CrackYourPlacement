class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort() # Sort the array to manage duplicates
        result = []
        
        def backtrack(start, target, current):
            if target == 0: # Base case: if we hit the target, add the current combination to the result
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue # Skip duplicates
                if candidates[i] > target:
                    break # If the candidate exceeds the target, stop the loop
                current.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current) # Move to the next candidate
                current.pop() # Backtrack by removing the last candidate
        
        backtrack(0, target, [])
        return result