class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count = 1
        j = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j
nums = [1, 1, 1, 2, 2, 3]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Output: {k}, nums = {nums[:k]}")
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k = solution.removeDuplicates(nums)
print(f"Output: {k}, nums = {nums[:k]}")