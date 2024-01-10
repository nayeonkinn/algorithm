import sys
from heapq import heappush, heappop

sys.stdin = open('input/1202-1.txt')  # 10, 164
input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()

answer = 0
temp = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        heappush(temp, -gems[0][1])
        heappop(gems)
    
    if temp:
        answer -= heappop(temp)

print(answer)