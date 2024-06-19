"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
 
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
         
# === Main === 
class Itterative:
    def threeSum(self, nums):
        ans = set()
        nums.sort()
        n = len(nums)
        for i in range (n-2):
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j+=1
                elif temp > 0:
                    k-=1
                else:
                    j+=1
        return ans
# === End Main ===

# # === Main === 
class BrureForce:
    def threeSum(self, nums):    
        ans=set()
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp=nums[i]+nums[j]+nums[k]
                    if temp==0:
                        ans.add((nums[i],nums[j],nums[k]))
        return ans
# # === End Main ===