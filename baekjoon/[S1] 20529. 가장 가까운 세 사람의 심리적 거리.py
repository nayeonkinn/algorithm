import sys
from itertools import combinations as comb
sys.stdin = open('input/20529.txt')
input = sys.stdin.readline

def d(A, B):
    return sum([A[i] != B[i] for i in range(4)])

T = int(input())
for tc in range(T):
    N = int(input())
    mbti = input().split()
    if len(mbti) > 32:
        print(0)
    else:
        ans = 12
        for c in set(list(comb(mbti, 3))):
            dist = d(c[0], c[1]) + d(c[0], c[2]) + d(c[1], c[2])
            ans = min(ans, dist)
        print(ans)
