class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
nums = [3, 2, 3]
solution = Solution()
print("Output:", solution.majorityElement(nums)) 
nums = [2, 2, 1, 1, 1, 2, 2]
print("Output:", solution.majorityElement(nums)) 