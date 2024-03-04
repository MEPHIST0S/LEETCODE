class Solution(object):
    def removeElement(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

# Example usage:
# Create an instance of Solution
sol = Solution()
# Input list
nums = [3, 2, 2, 3, 2, 4, 5, 6]
# Value to be removed
val = 2
# Call the removeElement method to remove all occurrences of val from nums
new_length = sol.removeElement(nums, val)
print("Modified List:", nums[:new_length])
print("Length of Modified List:", new_length)