import sys

sys.stdin = open('input/16472.txt')  # 4

N = int(input())
s = input()

word = {}
left, right = 0, 0
answer = 0

while right < len(s):
    if s[right] in word:
        word[s[right]] += 1
    else:
        word[s[right]] = 1

    while len(word) > N:
        word[s[left]] -= 1

        if not word[s[left]]:
            del word[s[left]]
            
        left += 1

    answer = max(answer, right - left + 1)
    right += 1

print(answer)