class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n > 0:
            if n % 2:
                answer += 1
            n //= 2
        return answer