import sys

sys.stdin = open('input/11866.txt') # <3, 6, 2, 7, 5, 1, 4>

N, K = map(int, input().split())

q = list(range(1, N + 1))
idx = 0
answer = []

while q:
    idx = (idx + K - 1) % len(q)
    answer.append(str(q.pop(idx)))

print('<' + ', '.join(answer) + '>')