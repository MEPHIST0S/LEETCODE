class Solution(object):
    def combine(self, n, k):
        arr = []
        nums = [0] * k

        def backtrack(pos, cur):
            if pos == k:
                arr.append(nums[:])
                return
            for i in range(cur, n-k+pos+2):
                nums[pos] = i
                backtrack(pos+1, i+1)

        backtrack(0, 1)
        return arr
    

"""
Time Complexity = O(n^k)
Space Complexity = O(n^k)
"""