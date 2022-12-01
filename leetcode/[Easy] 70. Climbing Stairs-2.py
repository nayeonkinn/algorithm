class Solution:
    memo = [False] * 46

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if Solution.memo[n]:
            return Solution.memo[n]
            
        Solution.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return Solution.memo[n]