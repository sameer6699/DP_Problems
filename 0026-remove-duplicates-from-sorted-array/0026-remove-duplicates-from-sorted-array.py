class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1        
        return k
solution = Solution()
nums1 = [1, 1, 2]
k1 = solution.removeDuplicates(nums1)
print(k1)
print(nums1[:k1])
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = solution.removeDuplicates(nums2)
print(k2)  
print(nums2[:k2])