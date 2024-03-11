class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

#Example of Usage!
solution = Solution()
numbers = [1, 2, 11, 5]
target = 6
print(solution.twoSum(numbers, target)) 