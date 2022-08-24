class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ''
        for i in range(len(s)):
            long = max(self.check(s, i, i), self.check(s, i, i + 1), long, key = len)
            
        return long
    
    def check(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return s[i + 1:j]