import sys
sys.stdin = open('input/16236-1.txt') # 0, 3, 14, 60, 48, 39

def bfs(shark, size, ate, time):
    global answer
    queue = [shark]
    visited = [[0] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = 1
    fish = []

    while not fish:
        if not queue:
            return

        for _ in range(len(queue)):
            i, j = queue.pop(0)

            for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                di += i
                dj += j
                if 0 <= di < N and 0 <= dj < N and ocean[di][dj] <= size and visited[di][dj] == 0:
                    visited[di][dj] = visited[i][j] + 1
                    queue.append((di, dj))
                    if 0 < ocean[di][dj] < size:
                        fish.append((di, dj))
    
    i, j = sorted(fish)[0]
    ocean[i][j] = 0
    ate += 1
    if ate == size:
        size += 1
        ate = 0
    answer = time + visited[i][j] - 1
    bfs((i, j), size, ate, answer)

N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9:
            shark = (i, j)
            ocean[i][j] = 0
answer = 0
bfs(shark, 2, 0, 0)
print(answer)
