class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        sentence = ''
        for char in paragraph:
            if char in "!?',;.":
                sentence += ' '
            else:
                sentence += char
        words = sentence.split()

        count = {}
        for word in words:
            count[word.lower()] = count.get(word.lower(), 0) + 1
        for ban in banned:
            count.pop(ban, 0)
        count = sorted(count, key = lambda x: count[x], reverse = True)
        
        return count[0]