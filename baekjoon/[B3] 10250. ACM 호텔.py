import sys
sys.stdin = open('input/10250.txt')  # 402 1203

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    floor = N % H or H
    number = N // H + 1 if N % H else N // H

    print(floor * 100 + number)
