class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Replace numbers that are out of range with a number greater than n
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Mark numbers present in the array by making the index of those numbers negative
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        # Step 3: Find the first index that has a positive number, the missing number is i + 1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all numbers from 1 to n are present, the missing number is n + 1
        return n + 1

# Driver code
solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))  # Output: 3
print(solution.firstMissingPositive([3, 4, -1, 1]))  # Output: 2
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))  # Output: 1
