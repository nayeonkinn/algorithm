import sys
from bisect import bisect_right

sys.stdin = open('input/16566.txt')  # 5  2  3  4  9

def union(a, b):
    if b >= m:
        return
    
    a = find(a)
    b = find(b)

    parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

n, m, k = map(int, input().split())
card = sorted(map(int, input().split()))
cs = list(map(int, input().split()))

parent = [i for i in range(m)]

for c in cs:
    idx = find(bisect_right(card, c))
    print(card[idx])
    union(idx, idx + 1)