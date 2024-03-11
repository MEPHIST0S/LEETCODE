class Solution(object):
    def fib(self, n):
        if not n:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
#Example of Usage!
solution = Solution()
n = 4
print("Fibbo for n = ", n, ":", solution.fib(n))