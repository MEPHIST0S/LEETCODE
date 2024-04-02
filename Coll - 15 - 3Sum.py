"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution(object):
    def threeSum(self, nums):
        ans = set()
        nums.sort()
        n = len(nums)
        for i in range (n-2):
            j = i + 1
            k = n - 1
            while j<k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    j+=1
                    ans.add((nums[i], nums[j], nums[k]))
                elif temp > 0:
                    k-=1
                else:
                    j+=1
        return ans
    
#Example of Usage!
solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums))

"""
Time Complexity - O(n^2)
Space Complexity - O(n^2)
"""