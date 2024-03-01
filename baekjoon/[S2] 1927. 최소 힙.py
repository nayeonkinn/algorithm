import heapq, sys

sys.stdin = open('input/1927.txt')  # 0  1  2  12345678  0
input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(hq, x)
    elif hq:
        print(heapq.heappop(hq))
    else:
        print(0)