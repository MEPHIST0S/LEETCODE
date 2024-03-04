class Solution(object):
    def twoSum(self, nums, target):
        save = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in save:
                return [save[diff], i]
            save[nums[i]] = i

#Example of Usage
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))