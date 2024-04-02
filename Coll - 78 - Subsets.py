"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution(object):
    def subset(self, nums):
        arr = [[]]
        for j in nums:
            arr += [i + [j] for i in arr]
        return arr

#Example of Usage!
solution = Solution()
nums = [1, 2, 3]
print(solution.subset(nums))

"""
Time Complexity = O(2^n)
Space Complexity = O(2^n)
"""