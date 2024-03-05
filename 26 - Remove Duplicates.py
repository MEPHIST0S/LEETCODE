class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

#Example of Usage!
solution = Solution()
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print("List:", nums)
result_length = solution.removeDuplicates(nums)
print("Length:", result_length)
print("List:", nums[:result_length])