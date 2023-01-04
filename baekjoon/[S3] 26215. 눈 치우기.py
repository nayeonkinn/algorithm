import heapq as hq
import sys
sys.stdin = open('input/26215-1.txt')  # 3, 5, -1, 1440

n = int(input())
snow = list(map(lambda x: -int(x), input().split()))
hq.heapify(snow)
answer = 0
while len(snow) > 1:
    a, b = hq.heappop(snow), hq.heappop(snow)
    answer += abs(b)
    hq.heappush(snow, a - b)
answer -= snow[0]
print(answer) if answer < 1441 else print(-1)
