import sys
from itertools import permutations
sys.stdin = open('input/15663-1.txt')  # 2  4, 1 7  1 9  7 1  7 9  9 1  9 7  9 9, 1 1 1 1

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for p in sorted(set(permutations(nums, m))):
    print(*p)