import sys
from itertools import combinations as c
sys.stdin = open('input/6603.txt')

while True:
    k, *S = map(int, input().split())
    if k == 0:
        break

    for combi in list(c(S, 6)):
        print(*combi)
    print()
