import sys

sys.stdin = open('input/11047-1.txt')  # 6, 12
input = sys.stdin.readline

N, K = map(int, input().split())
coins = iter([int(input()) for _ in range(N)][::-1])

answer = 0

while K:
    coin = coins.__next__()
    if K >= coin:
        answer += K // coin
        K %= coin