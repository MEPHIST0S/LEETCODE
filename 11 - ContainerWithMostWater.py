class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            curr = min(height(left), height(right)) * (right - left)
            ans = max(curr, ans)
            if height(left) < height(right):
                left += 1
            else:
                right -= 1
        return ans