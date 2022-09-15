from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        word = deque()
        for char in s:
            if char in word:
                while char != word.popleft():
                    pass
            word.append(char)
            if len(word) > cnt:
                cnt = len(word)
        return cnt