import sys
sys.stdin = open('input/4861.txt', 'r')

def Palindrome(words, N, M):
    for i in range(N):
        for j in range(N - M + 1):
            word = words[i][j:j + M + 1]
            if word == word[::-1]:
                return word
    words = [''.join([words[j][i] for j in range(N)]) for i in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            word = words[i][j:j + M + 1]
            if word == word[::-1]:
                return word

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    words = [''.join(list(input())) for _ in range(N)]
    print(f'#{tc + 1} {Palindrome(words, N, M)}')