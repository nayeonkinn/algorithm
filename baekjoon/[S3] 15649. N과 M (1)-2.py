from itertools import permutations
import sys
sys.stdin = open('input/15649-1.txt')

n, m = map(int, input().split())
for p in permutations([i + 1 for i in range(n)], m):
    print(*p)
