import sys
import math

sys.stdin = open('input/17266-1.txt')  # 2, 3

n = int(input())
m = int(input())
pos = list(map(int, input().split()))

answer = max(pos[0], n - pos[-1])

for i in range(m - 1):
    answer = max(answer, math.ceil((pos[i + 1] - pos[i]) / 2))

print(answer)