class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
solution.rotate(nums, k)
print("Output:", nums) 
nums = [-1, -100, 3, 99]
k = 2
solution.rotate(nums, k)
print("Output:", nums)