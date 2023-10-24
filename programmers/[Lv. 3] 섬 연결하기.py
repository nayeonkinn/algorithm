def solution(n, costs):
    costs_arr = [[0] * n for _ in range(n)]
    for s, e, c in costs:
        costs_arr[s][e] = c
        costs_arr[e][s] = c
    
    connected = [False] * n
    connected[0] = True
    
    answer = 0
    while not all(connected):
        cost = 1e9
        for i in range(n):
            if connected[i]:
                for j in range(n):
                    if j != i and not connected[j] and costs_arr[i][j] and costs_arr[i][j] < cost:
                        cost = costs_arr[i][j]
                        cost_idx = j
        
        connected[cost_idx] = True
        answer += cost
    
    return answer


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs)) # 4
