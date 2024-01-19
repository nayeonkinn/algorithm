import sys

sys.stdin = open('input/2098.txt')  # 35
input = sys.stdin.readline

def dfs(x, visited):  # x: 현재 노드, visited: 현재 노드 포함해서 지금까지 방문한 노드 정보 (ex. 0, 2번 노드 방문 시 0b101)
    if visited == (1 << n) - 1:  # 모든 노드를 방문했다면
        if graph[x][0]:  # 길이 있다면
            return graph[x][0]  # 현재 노드에서 0번 노드로 돌아가는 거리 반환
        else:  # 길이 없다면
            return 1e9  # 최적이 될 수 없도록 INF 반환
    
    if dp[x][visited]:  # 값이 있다면 = 이미 방문하여 연산을 완료했다면
        return dp[x][visited]  # 이미 계산된 값을 반환 (memoization)
    dp[x][visited] = 1e9  # 값이 없다면 다음 코드에서 min 계산을 위해 INF로 초기화

    for y in range(1, n):  # 0번 노드는 이미 방문하였으니 1번 노드부터 돌면서
        if not graph[x][y]:  # 길이 없다면 넘어감
            continue

        if visited & (1 << y):  # 이미 방문한 노드라면 넘어감
            continue
        
        dp[x][visited] = min(dp[x][visited], dfs(y, visited | (1 << y)) + graph[x][y])
        # x까지 방문한 경우의 최적 이동거리 = min(이전 y로 연산한 값, 이번 y까지 방문한 경우의 최적 이동거리 + x에서 y 거리)

    return dp[x][visited]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (1 << n) for _ in range(n)]
# dp[x][visited]: 지금 x에 있고 visited를 방문했을 때, 남은 노드를 최적 경로로 방문했을 때의 이동거리

# 이때 dp를 INF로 초기화하면 방문하지 않은 노드와 방문했지만 길이 없는 노드를 구분할 수 없어 이미 방문한 노드를 계속 방문 (시간초과)
# -> 0으로 초기화한 뒤 dfs 내에서 이미 방문한 노드는 넘어가고, 방문하지 않은 노드에서만 INF로 값 변경 후 DP 연산 수행하여 해결

print(dfs(0, 1))