class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        stack = []
        
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        
        return ''.join(stack)