class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n, -1, -1):
            for j in range(n - i):
                sub = s[j:j + i + 1]
                if self.check(sub):
                    return sub

    def check(self, sub):
        n = len(sub)
        for i in range(n // 2):
            if sub[i] != sub[n - 1 - i]:
                return 0
        return 1