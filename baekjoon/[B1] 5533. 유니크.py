import sys

sys.stdin = open('input/5533-1.txt')  # 0  92  215  198  89, 0  63  63
input = sys.stdin.readline

N = int(input())
scores = list(zip(*[map(int, input().split()) for _ in range(N)]))

answer = [0] * N

for i in range(3):
    for j in range(N):
        if scores[i].count(scores[i][j]) == 1:
            answer[j] += scores[i][j]

print(*answer, sep='\n')