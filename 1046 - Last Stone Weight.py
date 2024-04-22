

class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones)>1:
            stones.sort()
            stones.append(abs(stones.pop()-stones.pop()))
        return stones[0]

#Example of Usage!
solution = Solution()
stones = [1, 2, 3, 4]
print(solution.lastStoneWeight(stones))

"""
Time Complexity = 
Space Complexity = 
"""