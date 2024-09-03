from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        nums.sort() 
        result = []
        backtrack(0)
        return result
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 1, 2]
    print(f"Input: {nums1}\nOutput: {solution.permuteUnique(nums1)}\n")
    nums2 = [1, 2, 3]
    print(f"Input: {nums2}\nOutput: {solution.permuteUnique(nums2)}\n")
