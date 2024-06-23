class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return      
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1        
        if i >= 0: 
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]     
        nums[i + 1:] = reversed(nums[i + 1:])

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print(nums)   
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    print(nums)
    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    print(nums) 