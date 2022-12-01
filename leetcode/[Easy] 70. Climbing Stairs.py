class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [False] * 46
        
        def factorial(n):
            if n < 2:
                return 1
            if memo[n]:
                return memo[n]
            
            memo[n] = n * factorial(n - 1)
            return memo[n]
        
        
        def combi(a, b):
            return factorial(a) / (factorial(a - b) * factorial(b))

        
        answer, a, b = 0, n, 0
        
        while a >= b:
            answer += combi(a, b)
            a -= 1
            b += 1
        
        return int(answer)