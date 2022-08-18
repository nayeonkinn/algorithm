import sys
sys.stdin = open('input/1219.txt', 'r')

def dfs(v):
    stack = [v]
    visited[v] = 1

    while stack:
        for w in road[v]:
            if visited[w] == 0:
                if w == 99:
                    return 1
                v = w
                stack.append(v)
                visited[v] = 1
                break
        else:
            stack.pop()
            if stack:
                v = stack[-1]
            else:
                return 0

for tc in range(1, 11):
    n = int(input().split()[1])
    temp = list(map(int, input().split()))
    road = [[] for _ in range(100)]
    i = 0
    while i < n * 2:
        road[temp[i]].append(temp[i + 1])
        i += 2

    visited = [0] * 100
    print(f'#{tc} {dfs(0)}')