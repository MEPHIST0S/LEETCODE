"""Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
         
# === Main === 
class Itterative:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return res
                if abs(temp - target) < abs(res - target):
                    res = target
                
                if temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
                else:
                    return res
        return res
# === End Main ===

# # === Main === 
class BrureForce:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    temp = nums[i] + nums[j] + nums[k]
                    if temp == target:
                        return temp
                    if abs(temp - target) < abs(res - target):
                        res = temp
                    
                    if temp < target:
                        j += 1
                    elif temp > target:
                        k -= 1
                    else:
                        return res
        return res
# # === End Main ===