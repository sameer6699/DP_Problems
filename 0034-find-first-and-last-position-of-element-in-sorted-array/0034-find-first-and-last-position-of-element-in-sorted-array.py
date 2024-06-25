class Solution(object):
    def searchRange(self, nums, target):
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        left_index = find_left(nums, target)
        right_index = find_right(nums, target)

        if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]
solution = Solution()
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(solution.searchRange(nums1, target1))  
nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(solution.searchRange(nums2, target2))  
nums3 = []
target3 = 0
print(solution.searchRange(nums3, target3))