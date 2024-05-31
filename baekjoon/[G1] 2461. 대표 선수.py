import sys, heapq

sys.stdin = open('input/2461-1.txt')  # 2, 70
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for x in arr:
    heapq.heapify(x)

rep = [(heapq.heappop(arr[i]), i) for i in range(N)]
heapq.heapify(rep)

max_val = max(rep)[0]
answer = max_val - rep[0][0]

while arr[idx := heapq.heappop(rep)[1]]:
    val = heapq.heappop(arr[idx])
    heapq.heappush(rep, (val, idx))    
    
    max_val = max(max_val, val)
    answer = min(answer, max_val - rep[0][0])

print(answer)