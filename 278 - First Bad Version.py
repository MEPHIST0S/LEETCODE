class Solution(object):
    def isBadVersion(self, version):
        # Предположим, что здесь есть реализация функции isBadVersion()
        pass
    
    def firstBadVersion(self, n):
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

if __name__ == "__main__":
    n = int(input("Введите общее количество версий: "))
    bad_version = int(input("Введите номер первой плохой версии: "))
    
    solution = Solution()
    solution.isBadVersion = lambda version: version >= bad_version
    
    print("Первая плохая версия:", solution.firstBadVersion(n))