class Solution:
    def calPoints(self, operations):
        ans = []
        for i in operations:
            if i == "+":
                ans.append(ans[-1] + ans[-2])
            elif i == "D":
                ans.append(2 * ans[-1])
            elif i == "C":
                ans.pop()
            else:
                ans.append(int(i))
        return sum(ans)

#Example of Usage!
operations = ["5", "2", "C", "D", "+"]
solution = Solution()
print(solution.calPoints(operations))

"""
Time Complexity:
    Time complexity is linear because the algorithm iterates through each operation in the input list once.
Space Complexity:
    Space complexity is also linear because the additional space usage scales with the number of operations in the input list.
"""