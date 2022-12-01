class Solution:
    memo = [False] * 31
    
    def fib(self, n: int) -> int:        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if Solution.memo[n]:
            return Solution.memo[n]

        Solution.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return Solution.memo[n]