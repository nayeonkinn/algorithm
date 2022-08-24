class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            repr_word = str(sorted(list(word)))
            if not anagram.get(repr_word):
                anagram[repr_word] = []
            anagram[repr_word].append(word)

        return list(anagram.values())