import sys

input = sys.stdin.readline

def dfs(friend, move, i, j, cnt, path):
    global answer
    
    if move == 3:
        if friend == m - 1:
            answer = max(answer, cnt)
        else:
            dfs(friend + 1, 0, *friends[friend + 1], cnt, path + [friends[friend + 1]])
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj

        if 0 <= ni < n and 0 <= nj < n:
            temp = trees[ni][nj]
            trees[ni][nj] = 0
            dfs(friend, move + 1, ni, nj, cnt + temp, path + [[ni, nj, temp, cnt + temp]])
            trees[ni][nj] = temp

n, m = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]
friends = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

answer = 0

for fi, fj in friends:
    answer += trees[fi][fj]
    trees[fi][fj] = 0

dfs(0, 0, *friends[0], answer, [friends[0]])

print(answer)