import sys
sys.stdin = open('input/12865.txt') # 14

n, k = map(int, input().split())
table = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, input().split())
    for j in range(k, -1, -1):
        if j + w <= k:
            table[j + w] = max(table[j + w], table[j] + v)

print(max(table))
