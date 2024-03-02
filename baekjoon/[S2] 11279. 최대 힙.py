import heapq, sys

sys.stdin = open('input/11279.txt')  # 0  2  1  3  2  1  0  0
input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(hq, -x)
    elif hq:
        print(-heapq.heappop(hq))
    else:
        print(0)