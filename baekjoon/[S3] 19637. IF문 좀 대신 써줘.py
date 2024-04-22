import sys

sys.stdin = open('input/19637-1.txt')  # WEAK  WEAK  WEAK  NORMAL  NORMAL  NORMAL  STRONG  STRONG, B  B  C  C  C
input = sys.stdin.readline

n, m = map(int, input().split())
title = list(map(lambda x: (x[0], int(x[1])), [input().split() for _ in range(n)]))
power = [int(input()) for _ in range(m)]

for p in power:
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2

        if p > title[mid][1]:
            left = mid + 1
        else:
            right = mid - 1
    
    print(title[left][0])