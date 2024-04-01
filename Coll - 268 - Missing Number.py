"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

class Solution(object):
    def missingNumber(self, nums):
        total = 0
        for i in range (len(nums) + 1):
            total += i
        return total - sum(nums)
    
#or

class AlternativeSol(object):
    def missingNum(self, nums):
        length = len(nums)
        total = length * (length + 1)/2
        return total - sum(nums)