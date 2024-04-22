"""
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

#Nested Solution
class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] == nums[j]:
                    count +=1
        return count
    
#Example of Usage!
solution = Solution()
nums = [1, 1, 2, 3, 3, 2]
print("Nested Way: ", solution.numIdenticalPairs(nums))

"""
Time Complexity:
    O(n^2) because nested loop
Space Complexity:
    O(1) because no additional space is needed
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        pairs = [0]*101
        for i in nums:
            count += pairs[i]
            pairs[i] += 1
        return count

#Example of Usage!
solution = Solution()
num = [1, 1, 2, 3, 3]
print("Linear Way: ", solution.numIdenticalPairs(num))           

"""
Time Complexity:
    O(n) because we have 1 loop that mean we go through list once
Space Complexity:
    O(1) because no additional space is needed
"""