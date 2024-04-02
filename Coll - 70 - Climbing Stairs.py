"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        initial = 0
        final = 1
        for _ in range (n):
            initial, final = final, initial + final
        return final

#Example of Usage!
solution = Solution()
n = 10
print(solution.climbStairs(n))

"""
Time Complexity - O(n)
Space Complexity - O(1)
"""