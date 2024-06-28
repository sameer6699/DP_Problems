class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(remaining, start, path, result):
            if remaining == 0:
                result.append(list(path))
                return
            elif remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i, path, result)
                path.pop()       
        result = []
        backtrack(target, 0, [], result)
        return result
solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  
print(solution.combinationSum([2, 3, 5], 8))    
print(solution.combinationSum([2], 1))          