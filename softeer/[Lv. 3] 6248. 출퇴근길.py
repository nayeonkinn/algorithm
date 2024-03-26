import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now, adj, visited):
    if visited[now]:
        return
    
    visited[now] = True
    for node in adj[now]:
        dfs(node, adj, visited)

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
adj_r = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj_r[y].append(x)

S, T = map(int, input().split())

# 출근길
from_S = [False] * (n + 1)
from_S[T] = True
dfs(S, adj, from_S)  # S에서 X

to_T = [False] * (n + 1)
dfs(T, adj_r, to_T)  # X에서 T

# 퇴근길
from_T = [False] * (n + 1)
from_T[S] = True
dfs(T, adj, from_T)  # T에서 X

to_S = [False] * (n + 1)
dfs(S, adj_r, to_S)  # X에서 S

answer = -2
for i in range(1, n + 1):
    if from_S[i] and to_T[i] and from_T[i] and to_S[i]:
        answer += 1
print(answer)