import sys
sys.stdin = open('input/1216.txt')

def palindrome(words):
    words2 = [''.join([words[j][i] for j in range(100)]) for i in range(100)]
    for length in range(100, 0, -1):
        for r in range(100):
            for c in range(100 - length + 1):
                word = words[r][c:length + c]
                if word == word[::-1]:
                    return length
                word = words2[r][c:length + c]
                if word == word[::-1]:
                    return length

for t in range(10):
    input()
    words = [input() for _ in range(100)]
    print(f'#{t + 1} {palindrome(words)}')