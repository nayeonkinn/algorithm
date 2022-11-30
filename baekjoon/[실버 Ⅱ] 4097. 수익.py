import sys
sys.stdin = open('input/4097.txt')


import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if not n: break
    
    profit = [int(input()) for _ in range(n)]
    for i in range(1, n):
        profit[i] = max(profit[i], profit[i - 1] + profit[i])

    print(max(profit))
