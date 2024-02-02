import sys
from bisect import bisect_left

sys.stdin = open('input/12015.txt')  # 4
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

bs = [arr[0]]

for a in arr[1:]:
    if a <= bs[-1]:
        bs[bisect_left(bs, a)] = a
    else:
        bs.append(a)

print(len(bs))