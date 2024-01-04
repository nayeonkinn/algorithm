n = int(input())

answer = 0
visited = [False] * n

def possible(queens, j):
    for qi, qj in enumerate(queens):
        if qj == j or abs(qi - len(queens)) == abs(qj - j):
            return False
    return True

def dfs(queens):
    global answer

    if len(queens) == n:
        answer += 1
        return
    
    for queen in range(n):
        if not visited[queen] and possible(queens, queen):
            visited[queen] = True
            dfs(queens + [queen])
            visited[queen] = False

dfs([])

print(answer)