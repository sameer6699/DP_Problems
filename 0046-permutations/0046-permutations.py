from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Resultant list to store all the permutations
        result = []
        
        # Helper function to perform backtracking
        def backtrack(start):
            # If the current permutation is complete, add a copy of it to the result
            if start == len(nums):
                result.append(nums[:])
                return
            
            # Swap each element with the current position and generate all permutations
            for i in range(start, len(nums)):
                # Swap the elements
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively generate permutations with the next element fixed
                backtrack(start + 1)
                
                # Backtrack by swapping the elements back
                nums[start], nums[i] = nums[i], nums[start]
        
        # Start backtracking from the first index
        backtrack(0)
        return result

# Driver code
solution = Solution()
print(solution.permute([1, 2, 3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(solution.permute([0, 1]))     # Output: [[0,1],[1,0]]
print(solution.permute([1]))        # Output: [[1]]
