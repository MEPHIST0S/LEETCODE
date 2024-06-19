class Itterative:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        check = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    check[i][j] = 1 + check[i + 1][j + 1]
                else:
                    check[i][j] = max(check[i + 1][j], check[i][j + 1])
        return check[0][0]

from functools import cache   
class Recursive:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def find(r, c):
            if r >= len(text1) or c >= len(text2):
                return 0
            ans = 0
            if text1[r] == text2[c]:
                ans += 1 + find(r + 1, c + 1)
            else:
                ans += max(find(r + 1, c), find(r, c + 1))
            return ans
        return find(0, 0)