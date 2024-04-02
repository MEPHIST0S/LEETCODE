#Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                string1 = s[:left] + s[left+1:]
                string2 = s[:right] + s[right+1:]
                return string1 == string1[::-1] or string2 == string2[::-1]
            left += 1
            right -= 1
        return True

#Example of Usage!
solution = Solution()
s = "aba"
print(solution.validPalindrome(s))

"""
Time Complexity = O(n)
Space Complexity = O(n)
"""