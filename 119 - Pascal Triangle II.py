class Itterative:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        check = [1, 1]
        while rowIndex >= 2:
            rowIndex -= 1
            newcheck = [1] * (len(check) + 1)
            for i in range(0, len(check) - 1):
                newcheck[i + 1] = check[i] + check[i + 1]
            check = newcheck
        return check

class Recursive:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        def dp(check, i):
            if i == rowIndex:
                return check
            temp = [1] * (len(check) + 1)
            for i in range(1, len(check)):
                temp[i] = check[i - 1] + check[i]
            return dp(temp, i + 1)
        return dp([1, 1], 0)