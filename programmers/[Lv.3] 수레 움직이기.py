red_end = None
blue_end = None

red_visited = None
blue_visited = None

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

answer = 1e9

def dfs(maze, red_now, blue_now, cnt):
    global answer, red_end, blue_end

    if cnt > answer:
        return

    if red_now == red_end and blue_now == blue_end:
        answer = min(answer, cnt)
        return

    if red_now == red_end:
        for di, dj in delta:
            ni, nj = blue_now[0] + di, blue_now[1] + dj
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and not blue_visited[ni][nj] and maze[ni][nj] != 5 and (ni, nj) != red_now:
                blue_visited[ni][nj] = True
                dfs(maze, red_now, (ni, nj), cnt + 1)
                blue_visited[ni][nj] = False

    elif blue_now == blue_end:
        for di, dj in delta:
            ni, nj = red_now[0] + di, red_now[1] + dj
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and not red_visited[ni][nj] and maze[ni][nj] != 5 and (ni, nj) != blue_now:
                red_visited[ni][nj] = True
                dfs(maze, (ni, nj), blue_now, cnt + 1)
                red_visited[ni][nj] = False

    else:
        for red_di, red_dj in delta:
            red_ni, red_nj = red_now[0] + red_di, red_now[1] + red_dj
            if 0 <= red_ni < len(maze) and 0 <= red_nj < len(maze[0]) and not red_visited[red_ni][red_nj] and maze[red_ni][red_nj] != 5:
                for blue_di, blue_dj in delta:
                    blue_ni, blue_nj = blue_now[0] + blue_di, blue_now[1] + blue_dj
                    if 0 <= blue_ni < len(maze) and 0 <= blue_nj < len(maze[0]) and not blue_visited[blue_ni][blue_nj] and maze[blue_ni][blue_nj] != 5:
                        if (red_ni, red_nj) != (blue_ni, blue_nj) and not ((red_ni, red_nj) == blue_now and (blue_ni, blue_nj) == red_now):
                            red_visited[red_ni][red_nj] = True
                            blue_visited[blue_ni][blue_nj] = True
                            dfs(maze, (red_ni, red_nj), (blue_ni, blue_nj), cnt + 1)
                            red_visited[red_ni][red_nj] = False
                            blue_visited[blue_ni][blue_nj] = False

def solution(maze):
    global answer, red_end, blue_end, red_visited, blue_visited

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)

    red_visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    blue_visited = [[False] * len(maze[0]) for _ in range(len(maze))]

    red_visited[red_start[0]][red_start[1]] = True
    blue_visited[blue_start[0]][blue_start[1]] = True

    dfs(maze, red_start, blue_start, 0)

    if answer == 1e9:
        answer = 0

    return answer