class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for j in jewels:
            cnt += stones.count(j)
        return cnt
