class Solution(object):
    def fourSum(self, nums, target):
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return ans  