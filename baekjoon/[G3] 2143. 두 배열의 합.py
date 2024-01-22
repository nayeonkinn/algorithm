import sys
from collections import defaultdict

sys.stdin = open('input/2143.txt')  # 7
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

answer = 0

d = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        d[sum(A[i:j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        answer += d[T - sum(B[i:j + 1])]

print(answer)