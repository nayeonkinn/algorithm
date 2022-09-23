import sys
sys.stdin = open('input/2105.txt')

def dfs(i, j, turn, dessert, start):
    global answer
    if turn == 3 and (i, j) == start:
        answer = max(len(dessert) - 1, answer)
        return

    for d in delta[turn:turn + 2]:
        di = i + d[0]
        dj = j + d[1]
        if 0 <= di < N and 0 <= dj < N and cafe[di][dj] not in dessert[1:]:
            if d == delta[turn]:
                dfs(di, dj, turn, dessert + [cafe[di][dj]], start)
            else:
                dfs(di, dj, turn + 1, dessert + [cafe[di][dj]], start)
 
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    delta = ((1, 1), (1, -1), (-1, -1), (-1, 1))
    answer = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, [cafe[i][j]], (i, j))
    print(f'#{t} {answer}')
