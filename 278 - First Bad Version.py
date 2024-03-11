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
    
n = 5