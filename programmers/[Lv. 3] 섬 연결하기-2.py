import heapq

# prim algorithm
def solution(n, costs):
    costs_arr = [[0] * n for _ in range(n)]
    for s, e, c in costs:
        costs_arr[s][e] = c
        costs_arr[e][s] = c
    
    answer = 0
    connected = [False] * n    
    heap = []
    heapq.heappush(heap, [0, 0])
    
    while heap:
        weight, node = heapq.heappop(heap)
        if not connected[node]:
            connected[node] = True
            answer += weight
            for i in range(n):
                if not connected[i] and costs_arr[node][i]:
                    heapq.heappush(heap, [costs_arr[node][i], i])
    
    return answer


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs)) # 4
