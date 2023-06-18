import sys, heapq
sys.stdin = open('input/1655.txt')
input = sys.stdin.readline

n = int(input())
left, right = [], []
for _ in range(n):
    if len(left) == len(right):
        heapq.heappush(left, -int(input()))
    else:
        heapq.heappush(right, int(input()))
    
    if right and -left[0] > right[0]:
        left_max = heapq.heappop(left)
        right_min = heapq.heappop(right)

        heapq.heappush(left, -right_min)
        heapq.heappush(right, -left_max)
    
    print(-left[0])
